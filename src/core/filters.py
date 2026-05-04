from core.models import VideoRecord


def is_clickbait(record: VideoRecord) -> bool:
    return record.ctr > 15 and record.retention_rate < 40


def filter_clickbait(records: list[VideoRecord]) -> list[VideoRecord]:
    return [r for r in records if is_clickbait(r)]
