from abc import ABC, abstractmethod
from core.models import VideoRecord


class Report(ABC):
    @abstractmethod
    def generate(self, data: list[VideoRecord]) -> list[VideoRecord]:
        pass