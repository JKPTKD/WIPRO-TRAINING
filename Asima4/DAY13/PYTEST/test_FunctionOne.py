def setup_function():
    print('\nsetup fuction called before any tests')
 
def teardown_function():
    print('\ntearup function called after all tests')
 
def test_funOne():
    print('running funOne')
    assert True
 
def test_funTwo():
    print('\nrunning funTwo')
    assert True
 
def test_funThree():
    print('\nrunning funThree')
    assert True
 