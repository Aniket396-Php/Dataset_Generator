import time
from tqdm import tqdm
from collections import deque

from src.config import config
from src import constants

from src.prompt_builder import PromptBuilder

from src.ollama_client import OllamaClient

from src.json_parser import JSONParser

from src.duplicate_detector import DuplicateDetector

from src.csv_manager import CSVManager

from src.checkpoint import CheckpointManager

from src.validator import Validator

from src.logger import logger

class DatasetGenerator:
    def __init__(self):
        self.client = OllamaClient()
        self.detector = DuplicateDetector()
        self.csv_mgr = CSVManager()
        self.checkpoint_mgr = CheckpointManager()
        self.recent_questions = deque(maxlen=20)
        
        state = self.checkpoint_mgr.load()
        self.generated_count = state["generated_count"]
        self.batch_number = state["batch_number"]
        
        existing_data = self.csv_mgr.load_existing()
        for row in existing_data:
            q = row[constants.KEY_QUESTION]
            self.detector.add(q)
            self.recent_questions.append(q)
            
        self.generated_count = len(self.detector.seen)
        logger.info(constants.MSG_INIT)
        
    def run(self):
        target = config.generation.target_count
        
        with tqdm(total=target, initial=self.generated_count, desc="Generating QA pairs") as pbar:
            while self.generated_count < target:
                self.batch_number += 1
                
                logger.info(constants.MSG_START_BATCH.format(batch_num=self.batch_number))
                success = self._process_batch()
                
                if success:
                    self.checkpoint_mgr.save(self.generated_count, self.batch_number)
                    pbar.n = self.generated_count
                    pbar.refresh()
                
        logger.info(constants.MSG_COMPLETE.format(total=self.generated_count))
        
    def _process_batch(self) -> bool:
        prompt = PromptBuilder.build_prompt(set(self.recent_questions))
        
        for attempt in range(1, config.api.max_retries + 1):
            try:
                response = self.client.generate(prompt)
                pairs = JSONParser.parse(response)
                
                valid_pairs = []
                for pair in pairs:
                    if not Validator.validate_pair(pair):
                        logger.warning(constants.MSG_VALIDATION_FAILED.format(reason="Format/Length"))
                        continue
                        
                    q = pair[constants.KEY_QUESTION]
                    if self.detector.is_duplicate(q):
                        logger.warning(constants.MSG_DUPLICATE_SKIPPED.format(question=q))
                        continue
                        
                    valid_pairs.append({
                        constants.KEY_QUESTION: q,
                        constants.KEY_ANSWER: pair[constants.KEY_ANSWER]
                    })
                    
                    self.detector.add(q)
                    self.recent_questions.append(q)
                    
                if valid_pairs:
                    self.csv_mgr.save_batch(valid_pairs)
                    self.generated_count += len(valid_pairs)
                    logger.info(constants.MSG_BATCH_SUCCESS.format(count=len(valid_pairs), batch_num=self.batch_number))
                    return True
                else:
                    logger.warning(f"Batch {self.batch_number} yielded 0 valid/unique pairs.")
                    
            except Exception as e:
                logger.error(constants.MSG_BATCH_ERROR.format(batch_num=self.batch_number, error=str(e)))
                if attempt < config.api.max_retries:
                    logger.info(constants.MSG_BATCH_RETRY.format(batch_num=self.batch_number, attempt=attempt, max_retries=config.api.max_retries))
                    time.sleep(config.api.retry_delay)
                else:
                    logger.error(constants.MSG_BATCH_FAILED.format(batch_num=self.batch_number, retries=config.api.max_retries))
                    
        return False
