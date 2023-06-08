import inspect
import sys


def plus(a, b):
    if a == 0 and b == 0:
        raise ValueError('bad data')
    return a + b


def test_two_plus_two():
    assert plus(2, 2) == 4


def test_zero():
    assert plus(0, 0) == 0


def test_negative():
    assert plus(1, -1) == 0

