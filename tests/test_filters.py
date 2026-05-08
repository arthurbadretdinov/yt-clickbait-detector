from core.filters import filter_clickbait
from core.models import VideoRecord


def test_filter_clickbait(base_data: list[VideoRecord]) -> None:
    result = filter_clickbait(base_data)

    expected_count = sum(1 for v in base_data if v.ctr > 15 and v.retention_rate < 40)

    assert all(v.ctr > 15 for v in result)
    assert all(v.retention_rate < 40 for v in result)
    assert len(result) == expected_count
