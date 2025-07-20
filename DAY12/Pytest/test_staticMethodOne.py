import pytest
import subprocess
import sys
import os
from staticMethodOne import PasswordUtils
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'staticMethodOne.py')
@pytest.mark.parametrize("password, expected_strength", [
    ("testone", False), 
    ("testOne", False), 
    ("testone1", False), 
    ("testOne1", True), 
    ("TESTONE1", True), 
    ("testoneone1", False), 
    ("TESTONEONE", False), 
    ("testoneoneA", False), 
    ("testoneone1A", True), 
    ("ShorT1", False), 
    ("LongPass1", True),
    ("LongpasswOrd", False), 
    ("12345678", False), 
    ("a", False), 
    ("", False), 
])
def test_isstrong_logic(password, expected_strength):
    """
    Tests the core logic of the isstrong static method directly.
    """
    actual_strength = PasswordUtils.isstrong(password)
    assert actual_strength == expected_strength, \
        f"Password '{password}': Expected {expected_strength}, got {actual_strength}"
def test_script_output():
    expected_output = """password: testone is Weak
password: testOne#$ is Weak
"""
    try:
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH],
            capture_output=True,
            text=True,
            check=True 
        )
        actual_output = result.stdout

        print(f"\n--- Expected Output ---\n'{expected_output}'")
        print(f"\n--- Actual Output ---\n'{actual_output}'")

        assert actual_output == expected_output, \
            f"Output mismatch.\nExpected:\n'{expected_output}'\nActual:\n'{actual_output}'"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Script execution failed: {e.stderr}")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")