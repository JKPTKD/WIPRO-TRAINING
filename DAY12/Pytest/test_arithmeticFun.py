from arithmeticFun import add, sub
def test_AddFirst():
    assert add(10,20) == 30
def test_AddSecond():
    assert add(10,-20) == -10
def test_SubFirst():
    assert sub(10,-20) == 30
def test_SubSecond():
    assert sub(100,20) == 80