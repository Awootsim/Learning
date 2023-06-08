import pytest


def plus(a, b):
    if a == 0 and b == 0:
        raise ValueError('bad data')
    return a + b


@pytest.mark.parametrize('a,b,result', [(0, 0, 0), (2, 2, 4), (1, -1, 0)],
                         ids=['zero', 'positive', 'negative'])
def test_plus(a, b, result):
    assert plus(a, b) == result
