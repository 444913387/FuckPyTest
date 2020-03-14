
import pytest
class TestClass():

    def setup_class(self):
        print('setupclass')
    def teardown_class(self):
        print('teardownclass')


    def setup(self):
        print('func setup')
    def teardown(self):
        print('func teardown')

    def testa(self):
        print('testa')

    def testb(self):
        print('testb')

if __name__ == '__main__':
    pytest.main('-s','test_case.py')