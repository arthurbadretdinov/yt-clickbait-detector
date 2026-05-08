import pytest
from pathlib import Path
from contextlib import nullcontext as does_not_raise
from typing import ContextManager, Any

from infrastructure.reader import read_csv, read_csv_files


@pytest.mark.parametrize(
    "file_name, expectation",
    [
        ("stats1.csv", does_not_raise()),
        ("stats2.csv", does_not_raise()),
        ("file_not_found.csv", pytest.raises(FileNotFoundError)),
        ("invalid_types.csv", pytest.raises(ValueError)),
        ("missing_columns.csv", pytest.raises(ValueError)),
        ("bad_encoding.csv", pytest.raises(ValueError)),
    ],
)
def test_read_csv(file_name: str, expectation: ContextManager[Any]) -> None:
    with expectation:
        read_csv("data/" + file_name)


def test_read_csv_files_empty() -> None:
    result = read_csv_files([])

    assert result == []


def test_read_csv_files_single() -> None:
    file1 = Path("data/1.csv")
    file1.write_text("title,ctr,retention_rate\nA,20,30")

    result = read_csv_files([str(file1)])

    assert len(result) == 1


def test_read_csv_files() -> None:
    file1 = Path("data/1.csv")
    file1.write_text("title,ctr,retention_rate\nA,20,30")

    file2 = Path("data/2.csv")
    file2.write_text("title,ctr,retention_rate\nB,25,35")

    result = read_csv_files([str(file1), str(file2)])

    titles = [v.title for v in result]

    assert titles == ["A", "B"]
