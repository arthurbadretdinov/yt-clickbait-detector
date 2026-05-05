from core.models import VideoRecord
from core.filters import filter_clickbait
from core.sorting import sort_by_ctr_desc
from reports.base import Report


class ClickbaitReport(Report):
    def generate(self, data: list[VideoRecord]) -> list[VideoRecord]:
        clickbait_videos = filter_clickbait(data)
        return sort_by_ctr_desc(clickbait_videos)