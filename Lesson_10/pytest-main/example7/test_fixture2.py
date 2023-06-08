import os


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
