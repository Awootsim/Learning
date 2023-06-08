import pytest


def test_dict():
    a = dict(b=1)
    with pytest.raises(KeyError):
        a['b']