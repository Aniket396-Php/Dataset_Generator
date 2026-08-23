import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List

@dataclass
class APIConfig:
    base_url: str = "http://localhost:11434/v1"
    api_key: str = "ollama"
    model: str = "qwen3:8b"
    timeout: int = 1200
    max_retries: int = 5
    retry_delay: int = 3
    max_tokens: int = 4000

@dataclass
class GenerationConfig:
    target_count: int = 2100
    batch_size: int = 5
    temperature: float = 0.85
    min_answer_words: int = 20
    max_answer_words: int = 120

@dataclass
class SimilarityConfig:
    threshold: float = 85.0

@dataclass
class FileConfig:
    output_csv: Path = Path("data/viking_dataset.csv")
    checkpoint_json: Path = Path("checkpoint.json")
    log_file: Path = Path("generator.log")

@dataclass
class TopicConfig:
    topics: List[str] = field(default_factory=lambda: [
        "Viking Age", "Norse Society", "Kings", "Queens", "Jarls",
        "Exploration", "Leif Erikson", "Erik the Red", "Harald Fairhair",
        "Harald Hardrada", "Cnut the Great", "Ragnar Lothbrok",
        "Ivar the Boneless", "Ubba", "Halfdan", "England", "Ireland",
        "Scotland", "France", "Normandy", "Russia", "Byzantine Empire",
        "Varangians", "Trade", "Runes", "Longships", "Weapons", "Battles",
        "Daily Life", "Religion", "Norse Gods", "Conversion to Christianity",
        "Laws", "Thing Assemblies", "Economy", "Farming", "Settlements",
        "Archaeology", "Artifacts"
    ])
    question_styles: List[str] = field(default_factory=lambda: [
        "Who", "What", "Why", "When", "Where", "How", "Which",
        "Comparison", "Cause-effect", "Scenario", "Historical interpretation"
    ])

@dataclass
class AppConfig:
    api: APIConfig = field(default_factory=APIConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)
    similarity: SimilarityConfig = field(default_factory=SimilarityConfig)
    files: FileConfig = field(default_factory=FileConfig)
    topics: TopicConfig = field(default_factory=TopicConfig)

config = AppConfig()
