import os
import tempfile

import pytest


# cached if scope > function
@pytest.fixture(scope='function')
def create_file():
    print('BEFORE TEST')
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
    yield tmp.name
    print('AFTER TEST')
    if os.path.exists(tmp.name):
        os.remove(tmp.name)


@pytest.fixture
def read_file(create_file):
    with open(create_file, 'r') as file:
        return file.read()


@pytest.fixture
def first_fixture():
    return 1


@pytest.fixture
def second_fixture():
    return 2


@pytest.fixture
def main_fixture(first_fixture, second_fixture):
    return first_fixture + second_fixture


@pytest.fixture(autouse=True, scope='session')
def autouse_fixture():
    print('РАБОТАЮ ВСЕГДА!!!')
