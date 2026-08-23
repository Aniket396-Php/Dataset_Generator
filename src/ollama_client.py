from openai import OpenAI

from src.config import config
from src import constants

class OllamaClient:
    def __init__(self):
        self.client = OpenAI(
            base_url=config.api.base_url,
            api_key=config.api.api_key
        )
        
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=config.api.model,
            messages=[
                {"role": "system", "content": constants.SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=config.generation.temperature,
            max_tokens=config.api.max_tokens,
            timeout=config.api.timeout
        )
        return response.choices[0].message.content
