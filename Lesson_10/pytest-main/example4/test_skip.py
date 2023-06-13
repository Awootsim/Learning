import pytest


@pytest.mark.skip('в процессе')
def test_skip():
    raise ValueError('bad test')


class TestException:

    @pytest.mark.skip('чиним')
    def test(self):
        a = dict()
        a['b']

    def test(self):
        l = list()
        l[0]