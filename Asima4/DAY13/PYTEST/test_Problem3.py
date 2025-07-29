import pytest
@pytest.fixture
def userProfile():
    print("\nSetting up userProfile fixture...")
    profile = {
        'username': 'testuser123',
        'role': 'admin'
    }
    yield profile
    print("Tearing down userProfile fixture...")

def test_user_profile_values(userProfile):
    print(f"Inside test_user_profile_values: {userProfile}")
    assert 'username' in userProfile, "userProfile should contain a 'username' key"
    assert userProfile['username'] == 'testuser123', \
        f"Expected username 'testuser123', but got '{userProfile['username']}'"
    assert 'role' in userProfile, "userProfile should contain a 'role' key"
    assert userProfile['role'] == 'admin', \
        f"Expected role 'admin', but got '{userProfile['role']}'"
    assert isinstance(userProfile['username'], str), "Username should be a string"
    assert isinstance(userProfile['role'], str), "Role should be a string"