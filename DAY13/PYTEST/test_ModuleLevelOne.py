def setup_module():
    print('\nsetup module called before any tests')
 
def teardown_module():
    print('\ntearup module called after all tests')
 
def test_funOne():
    print('running funOne')
    assert True
 
def test_funTwo():
    print('\nrunning funTwo')
    assert True
 
def test_funThree():
    print('\nrunning funThree')
    assert True
 
 