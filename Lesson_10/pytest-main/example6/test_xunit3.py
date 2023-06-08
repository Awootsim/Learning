import os
import tempfile
from typing import Optional


class TestCRUD:

    file_name: Optional[str] = None

    @classmethod
    def setup_class(cls):
        print('SETUP CLASS')

    @classmethod
    def teardown_class(cls):
        print('TEARDOWN CLASS')

    def setup_method(self):
        print('setup method')
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False,
                                         dir=os.getcwd()) as tmp:
            tmp.write('test data')
            self.file_name = tmp.name

    def teardown_method(self):
        print('teardown method')
        os.remove(self.file_name)

    def test_read(self):
        with open(self.file_name, 'r') as file:
            assert 'test data' == file.read()

    def test_update(self):
        print('test update')

    def test_delete(self):
        print('test delete')
