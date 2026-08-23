from typing import Dict

from src.config import config
from src import constants

class Validator:
    @staticmethod
    def validate_pair(pair: Dict[str, str]) -> bool:
        if constants.KEY_QUESTION not in pair or constants.KEY_ANSWER not in pair:
            return False
            
        q = pair[constants.KEY_QUESTION].strip()
        a = pair[constants.KEY_ANSWER].strip()
        
        if not q or not a:
            return False
            
        words = len(a.split())
        if words < config.generation.min_answer_words or words > config.generation.max_answer_words:
            return False
            
        return True
