import subprocess
import sys
import os
import pytest

def test_nested_for_loop_output():
    script_path = os.path.join(os.path.dirname(__file__), 'nestedFor.py')
    expected_output = """a:0 1 2 3 4 5 6 7 8 9 
b:0 1 2 3 4 5 6 7 8 9 
c:0 1 2 3 4 5 6 7 8 9 
d:0 1 2 3 4 5 6 7 8 9 
e:0 1 2 3 4 5 6 7 8 9 
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