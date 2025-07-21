import pytest
 
@pytest.fixture
def sample():
    print('Setup Part of my Fixture')
    yield 100
    print('Teardown Part of my Fixture')
 
def test_funOne(sample):
    print('test_funOne() called')
    assert sample == 100
 
def test_funTwo(sample):
    print('test_funTwo() called')
    assert sample - 2 == 98
   
 