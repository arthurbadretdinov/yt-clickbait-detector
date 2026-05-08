from core.sorting import sort_by_ctr_desc
from core.models import VideoRecord


def test_sort_by_ctr_desc(base_data: list[VideoRecord]):
    result = sort_by_ctr_desc(base_data)

    ctrs = [v.ctr for v in result]

    assert ctrs == sorted(ctrs, reverse=True)
