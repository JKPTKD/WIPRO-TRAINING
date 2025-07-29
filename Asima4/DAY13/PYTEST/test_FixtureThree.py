import pytest
 
@pytest.fixture
def sample():
    print('Setup Part of my Fixture')
    yield 100
    print('Teardown Part of my Fixture')
   
@pytest.fixture
def dataTest():
    print('Setup Part of my Fixture')
    yield 10
    print('Teardown Part of my Fixture')
 
def test_funOne(sample):
    print('test_funOne() called')
    assert sample == 100
 
def test_funTwo(sample):
    print('test_funTwo() called')
    assert sample - 2 == 98
 
def test_funThree(dataTest):
    print('test_funThree() called')
    assert dataTest - 2 == 8
   
def test_funFour(dataTest):
    print('test_funFour() called')
    assert dataTest + 10 == 20
 