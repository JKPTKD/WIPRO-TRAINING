import pytest 
import sys 

#simple skip 
@pytest.mark.skip(reason='Functionality not implemented')
def test_funOne():
	pass 
		
#conditional skip
#@pytest.mark.skipif(condition, reason)
@pytest.mark.skipif(sys.platform != 'linux',reason='Specifically written for Linux')
def test_funTwo():
	pass 

#Programmatically skip (inside the test function)
def test_funThree():
	if 4 == 3 + 1:
		pytest.skip('Skipping funThree')	
	assert False
	
