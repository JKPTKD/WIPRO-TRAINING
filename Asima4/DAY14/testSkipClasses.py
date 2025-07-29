import pytest 

@pytest.mark.skip(reason='Trying to skip the whole class')
class TestClass:
    def test_One(self):
        print('test_One() from TestClass... ')

    def test_Two(self):
        print('test_Two() from TestClass... ')

    def test_Three(self):
        print('test_Three() from TestClass... ')