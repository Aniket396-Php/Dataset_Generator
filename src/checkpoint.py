import json
import os
import time
from typing import Dict, Any

from src.config import config

class CheckpointManager:
    def __init__(self):
        self.filepath = config.files.checkpoint_json
        
    def save(self, generated_count: int, batch_number: int):
        data = {
            "generated_count": generated_count,
            "batch_number": batch_number,
            "timestamp": time.time()
        }
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    def load(self) -> Dict[str, Any]:
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        return {"generated_count": 0, "batch_number": 0, "timestamp": 0}
