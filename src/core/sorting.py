from core.models import VideoRecord


def sort_by_ctr_desc(videos: list[VideoRecord]) -> list[VideoRecord]:
    return sorted(videos, key=lambda v: v.ctr, reverse=True)