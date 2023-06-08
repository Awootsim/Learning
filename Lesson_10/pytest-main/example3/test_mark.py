import pytest


@pytest.mark.smoke
def test_registry():
    pass


@pytest.mark.acceptance
def test_search():
    pass


@pytest.mark.id_check(123, 456)
def test_functional():
    pass


class TestBase:

    @pytest.mark.smoke
    def test_create_doc(self):
        pass

    @pytest.mark.acceptance
    def test_filter(self):
        pass


@pytest.mark.smoke
class TestSmoke:

    def test(self):
        pass
