def test_envValue(env):
	print(f'Printing from test_envValue() with "{env}"')
	assert env in ['dev', 'staging', 'prod'] 	
	
def test_examValue(exam):
	print(f'Printing from test_examValue() with "{exam}"')
	assert exam in ['unit', 'alpha', 'beta'] 