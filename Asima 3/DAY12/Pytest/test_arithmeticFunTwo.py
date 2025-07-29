from arithmeticFun import mult,divf
def test_mulFirst():
    assert mult(10,20) == 200
def test_MultSecond():
    assert mult(10,-20) == -200
def test_DivfFirst():
    assert divf(10,-20) == -0.5
def test_DivfSecond():
    assert divf(10,-20) == -0.5
def test_DivfThird():
    import pytest
    with pytest.raises(ZeroDivisionError):
        assert divf(100,0)
