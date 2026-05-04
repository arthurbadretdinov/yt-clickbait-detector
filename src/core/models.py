from dataclasses import dataclass

@dataclass
class VideoRecord:
    title: str
    ctr: float
    retention_rate: float