import subprocess
import sys
import os
import pytest

def test_module_interaction_output():

    script_path = os.path.join(os.path.dirname(__file__), 'usingModOne.py')
    expected_output = """data: Hello from moduleOne
Function One executed!
Function Two executed!
Function Three executed!
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
    except FileNotFoundError:
        pytest.fail(f"Could not find the script at {script_path}. Make sure usingModOne.py and moduleOne.py are in the same directory as the test file.")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")