from pytest import fixture
from functools import reduce

@fixture(scope='class')
def sampleData():
    print('setup class scoped...')
    yield [1,2,3]
    print('teardown class scoped...')
    
class TestClassOne:
    def test_One(self, sampleData):
        print('\ntestOne()...')
        assert sum(sampleData) == 6
        
    def test_Two(self, sampleData):
        print('\ntestTwo()...')
        assert reduce(lambda x, y:x*y,sampleData) == 6