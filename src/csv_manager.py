import csv
import os
from typing import List, Dict

from src.config import config
from src import constants

class CSVManager:
    def __init__(self):
        self.filepath = config.files.output_csv
        self._init_file()
        
    def _init_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', newline='', encoding=constants.FILE_ENCODING) as f:
                writer = csv.DictWriter(f, fieldnames=constants.CSV_COLUMNS)
                writer.writeheader()
                
    def save_batch(self, pairs: List[Dict[str, str]]):
        with open(self.filepath, 'a', newline='', encoding=constants.FILE_ENCODING) as f:
            writer = csv.DictWriter(f, fieldnames=constants.CSV_COLUMNS)
            writer.writerows(pairs)
            
    def load_existing(self) -> List[Dict[str, str]]:
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r', encoding=constants.FILE_ENCODING) as f:
            reader = csv.DictReader(f)
            return list(reader)
