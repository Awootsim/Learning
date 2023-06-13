import os
from typing import Optional

file_name: Optional[str] = None


def test_read(read_file):
    assert 'test data' == read_file
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
