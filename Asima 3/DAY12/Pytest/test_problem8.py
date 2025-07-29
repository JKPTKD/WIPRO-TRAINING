import pytest
import subprocess
import sys
import os
from Problem8 import evenGenerator
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'Problem8.py')
@pytest.mark.parametrize("start, end, expected_evens", [
    (1, 10, [2, 4, 6, 8, 10]),
    (0, 5, [0, 2, 4]),
    (1, 1, []), 
    (2, 2, [2]),
    (7, 9, [8]),
    (10, 10, [10]),
    (11, 10, []), 
    (-5, 5, [-4, -2, 0, 2, 4]), 
])
def test_even_generator_logic(start, end, expected_evens):

    actual_evens = list(evenGenerator(start, end)) 
    assert actual_evens == expected_evens, \
        f"For range ({start}, {end}): Expected {expected_evens}, got {actual_evens}"

def test_script_output():
    expected_output = """Even numbers using generator function:
2 4 6 8 10 
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