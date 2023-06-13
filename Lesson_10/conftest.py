import pytest
import datetime

@pytest.fixture(scope="class")
def class_fixture():
    start_time = datetime.datetime.now()
    print(f"Class setup: Start time - {start_time}")
    yield
    end_time = datetime.datetime.now()
    print(f"Class teardown: End time - {end_time}")

@pytest.fixture
def test_fixture():
    start_time = datetime.datetime.now()
    print(f"Test setup: Start time - {start_time}")
    yield
    end_time = datetime.datetime.now()
    print(f"Test teardown: End time - {end_time}")