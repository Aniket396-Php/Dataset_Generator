import random
from typing import Set

from src.config import config
from src import constants

class PromptBuilder:
    @staticmethod
    def build_prompt(recent_questions: Set[str]) -> str:
        topics = random.sample(config.topics.topics, k=min(5, len(config.topics.topics)))
        styles = random.sample(config.topics.question_styles, k=min(3, len(config.topics.question_styles)))
        
        recent_list = list(recent_questions)
        recent_text = "\n".join([f"- {q}" for q in recent_list]) if recent_list else "None"
        
        return constants.USER_PROMPT_TEMPLATE.format(
            batch_size=config.generation.batch_size,
            topics=", ".join(topics),
            styles=", ".join(styles),
            min_words=config.generation.min_answer_words,
            max_words=config.generation.max_answer_words,
            recent_questions=recent_text
        )
