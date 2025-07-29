import pytest
@pytest.mark.skip(reason='Trying to skip', allow_module_level=True)
 
 
def test_funModOne():
    print('funModOne()... called')
    assert True
 
def test_funModTwo():
    print('funModTwo()... called')
    assert True
 
def test_funModThree():
    print('funModThree()... called')
    assert True
 
 