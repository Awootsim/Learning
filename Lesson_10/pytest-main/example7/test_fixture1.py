import os
import tempfile
import pytest


@pytest.fixture(scope='function')
def create_file():
    print('BEFORE TEST')
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
    yield tmp.name
    print('AFTER TEST')
    if os.path.exists(tmp.name):
        os.remove(tmp.name)


def test_read(create_file):
    with open(create_file, 'r') as file:
        assert 'test data' == file.read()
    print('test read')


def test_update(create_file):
    with open(create_file, 'a') as file:
        file.write('test2')
    with open(create_file, 'r') as file:
        assert 'test2' in file.read()
    print('test update')


def test_delete(create_file):
    os.remove(create_file)
    assert not os.path.exists(create_file)
    print('test delete')
