import pytest


def plus(a, b):
    return a + b


@pytest.mark.parametrize('a,b,result', [(0, 0, 0), (2, 2, 4), (1, -1, 0)])
def test_plus(a, b, result):
    assert plus(a, b) == result
