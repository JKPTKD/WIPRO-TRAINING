import subprocess
import sys
import os
import pytest

def test_factorial_output():
    script_path = os.path.join(os.path.dirname(__file__), 'recurrssive.py')
    expected_output = "Factorial of 5 is: 120\n"

    try:
    
        result = subprocess.run(
            [sys.executable, script_path],
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

from recurrssive import factorial 

def test_factorial_base_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_positive_numbers():
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(7) == 5040 
