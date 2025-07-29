import pytest
 
@pytest.mark.xfail(reason='What ever reason')
def test_funFailOne():
    assert False
 
@pytest.mark.xfail(reason='Known Bug here')
def test_funFailTwo():
    assert 10 + 20 == 40