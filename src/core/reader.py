import csv
from core.models import VideoRecord


def read_csv(path: str) -> list[VideoRecord]:
    result: list[VideoRecord] = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            record = VideoRecord(
                title=row["title"],
                ctr=float(row["ctr"]),
                retention_rate=float(row["retention_rate"]),
            )
            result.append(record)

    return result
