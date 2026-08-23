from rapidfuzz import fuzz
from typing import Set

from src.config import config

class DuplicateDetector:
    def __init__(self):
        self.seen: Set[str] = set()
        
    def add(self, question: str):
        self.seen.add(self._normalize(question))
        
    def is_duplicate(self, question: str) -> bool:
        norm_q = self._normalize(question)
        if norm_q in self.seen:
            return True
            
        for existing in self.seen:
            if fuzz.ratio(norm_q, existing) >= config.similarity.threshold:
                return True
                
        return False
        
    def _normalize(self, text: str) -> str:
        return " ".join(text.lower().split())
