import pytest


@pytest.fixture
def prepare_data(request):
    a, b, result = request.param
    return a*2, b*2, result*2


def plus(a, b):
    if a == 0 and b == 0:
        raise ValueError('bad data')
    return a + b


@pytest.mark.parametrize('prepare_data', [(0, 0, 0), (2, 2, 4), (1, -1, 0)],
                         ids=['zero', 'positive', 'negative'],
                         indirect=True)
def test_plus(prepare_data):
    a, b, result = prepare_data
    assert plus(a, b) == result
