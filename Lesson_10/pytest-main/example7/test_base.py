import os
import tempfile


def create_tmp_file():
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
        return tmp.name


def delete_file_after_test(file_name):
    os.remove(file_name)


def test_read():
    file_name = create_tmp_file()
    try:
        with open(file_name, 'r') as file:
            assert 'test data' == file.read()
    finally:
        delete_file_after_test(file_name)


def test_update():
    file_name = create_tmp_file()
    try:
        with open(file_name, 'a') as file:
            file.write('test2')
        with open(file_name, 'r') as file:
            assert 'test2' in file.read()
    finally:
        delete_file_after_test(file_name)


def test_delete():
    file_name = create_tmp_file()
    os.remove(file_name)
    assert not os.path.isfile(file_name)

