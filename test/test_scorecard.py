import pytest
from src.ScoreCard import ScoreCard

cases = [
    pytest.param("12345123451234512345", 60, marks=[pytest.mark.scorecard, pytest.mark.regular], id="regular"),
    pytest.param("9-9-9-9-9-9-9-9-9-9-", 90, marks=[pytest.mark.scorecard, pytest.mark.zeros], id="zeros"),
    pytest.param("5/5/5/5/5/5/5/5/5/5/5", 150, marks=[pytest.mark.scorecard, pytest.mark.spare], id="spare"),
    pytest.param("X9-9-9-9-9-9-9-9-9-", 100, marks=[pytest.mark.scorecard, pytest.mark.strike], id="strike"),
    pytest.param("XXXXXXXXXXXX", 300, marks=[pytest.mark.scorecard, pytest.mark.perfect], id="perfect"),
    pytest.param("8/549-XX5/53639/9/X", 149, marks=[pytest.mark.scorecard, pytest.mark.complex], id="complex"),
]


@pytest.mark.parametrize("pins,expected", cases)
def test_scorecard(pins, expected):
    assert ScoreCard(pins).score() == expected
