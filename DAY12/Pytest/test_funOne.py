import subprocess
import sys
import os
import pytest

def test_function_outputs():
  
    script_path = os.path.join(os.path.dirname(__file__), 'funOne.py')

    expected_output = """Intro to functions in Python
This is outside the function
"""
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