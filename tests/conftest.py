import pytest
from core.models import VideoRecord


@pytest.fixture
def base_data() -> list[VideoRecord]:
    return [
        # valid clickbait (CTR > 15 AND retention < 40)
        VideoRecord("Good Video 1", 26, 12),
        VideoRecord("Good Video 3", 22, 34),
        VideoRecord("Good Video 2", 25, 25),
        # invalid: low CTR
        VideoRecord("Low ctr 1", 12, 19),
        VideoRecord("Low ctr 2", 15, 29),
        # invalid: high retention
        VideoRecord("High retention 1", 19, 45),
        VideoRecord("High retention 2", 19, 40),
        # invalid: low CTR and high retention
        VideoRecord("Low ctr and high retention", 9, 56),
    ]
