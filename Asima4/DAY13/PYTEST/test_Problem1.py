import pytest

@pytest.fixture
def dbConnection():
    print("\nSetting up dbConnection...")
    connection_string = "TestDBConnection"
    yield connection_string
    print("Tearing down dbConnection...")

def test_db_connection_is_not_none(dbConnection):
    print(f"Inside test_db_connection_is_not_none: {dbConnection}")
    assert dbConnection is not None, "Database connection should not be None"
    assert dbConnection == "TestDBConnection", "Database connection string mismatch"