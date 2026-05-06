import csv
from core.models import VideoRecord


def read_csv_files(paths: list[str]) -> list[VideoRecord]:
    result: list[VideoRecord] = []

    for path in paths:
        result.extend(read_csv(path))

    return result


def read_csv(path: str) -> list[VideoRecord]:
    try:
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

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    except UnicodeDecodeError:
        raise ValueError(f"Invalid file encoding (expected UTF-8): {path}")

    except KeyError as e:
        raise ValueError(f"Missing column in CSV: {e}")

    except ValueError as e:
        raise ValueError(f"Invalid data format in file: {path}: {e}")
