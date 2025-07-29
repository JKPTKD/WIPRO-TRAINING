data = []
def setup_module():
    print('\nsetup module called before any tests')
    global data
    data = [
        (3, 5, 8),
        (10, -20, -10),
        (0, 0, 0),
        (0, -10, 10)
    ]
 
def teardown_module():
    print('\ntearup module called after all tests')
    global data
    data = []
 
def test_funOne():
    print('running funOne')
    x,y, res = data[0]
    x1, y1, res1 = data[3]
    assert x + y == res
    assert x1 + y1 != res1
 
def test_funTwo():
    print('\nrunning funTwo')
    x,y, res = data[1]
    assert x + y == res
 
def test_funThree():
    print('\nrunning funThree')
    x,y, res = data[2]
    assert x + y == res
 
 