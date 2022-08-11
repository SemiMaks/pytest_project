import pytest

from utils import division


@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2),
                                                   (8, 4, 2),
                                                   (18, 9, 2)])
def test_division_good(a, b, expected_result):
    assert division(10, 5) == 2
