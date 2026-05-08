from reports.clickbait import ClickbaitReport
from core.models import VideoRecord


def test_clickbait_report(base_data: list[VideoRecord]) -> None:
    report = ClickbaitReport()

    result = report.generate(base_data)

    expected_count = sum(1 for v in base_data if v.ctr > 15 and v.retention_rate < 40)

    assert len(result) == expected_count
    assert all(v.ctr > 15 for v in result)
    assert all(v.retention_rate < 40 for v in result)

    ctrs = [v.ctr for v in result]
    assert ctrs == sorted(ctrs, reverse=True)
