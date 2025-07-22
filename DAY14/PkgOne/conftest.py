def pytest_addoption(parser):
    print('Inside pytest_addoption()')
    parser.addoption(
        '--env',action='store', default='dev', help='Evironment is /dev/staging/prod'
    )
    parser.addoption(
        '--exam',action='store', default='alpha', help='Test Evironment is unit/alpha/beta'
    )		
    
import pytest 
@pytest.fixture
def env(request):
    print('\nInside env() fixture')
    return request.config.getoption('--env')

@pytest.fixture
def exam(request):
    print('\nInside exam() fixture')
    return request.config.getoption('--exam')
