import pytest
import sys

@pytest.mark.xfail(reason='What ever reason')
def test_funFailOne():
    assert False 

@pytest.mark.xfail(reason='Known Bug here')
def test_funFailTwo():
    assert 10 + 20 == 40

@pytest.mark.xfail(sys.platform=='win32', reason='Platform specific')
def test_funFailThree():
    assert True

@pytest.mark.xfail(reason='Enforcing Failure', strict=True)
def test_funFailFour():
    assert False

def test_funModOne():
    print('funModOne()... called')
    assert True

def test_funModTwo():
    print('funModTwo()... called')
    assert True

def test_funModThree():
    print('funModThree()... called')
    assert True