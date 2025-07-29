import subprocess
import sys
import os
import pytest

def test_nested_function_output():
    script_path = os.path.join(os.path.dirname(__file__), 'nestedFunOne.py')
    expected_output = """In Outer(20)
coming out of Outer (20) --> __main__
In Inner(30)
Outer(20) --> returns 60
In Outer(10)
coming out of Outer (10) --> __main__
In Inner(20)
Outer(10) --> returns 40
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
