from tabulate import tabulate
from core.models import VideoRecord


def format_clickbait_report(videos: list[VideoRecord]) -> str:
    return tabulate(
        [(v.title, v.ctr, v.retention_rate) for v in videos],
        headers=["title", "ctr", "retention_rate"],
        tablefmt="grid",
    )