import pytest
import subprocess
import sys
import os
from Problem6 import create_multiplication_table
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'Problem6.py')
@pytest.mark.parametrize("start_num, end_num, expected_table", [
    (1, 1, [[1]]),
    (1, 2, [[1, 2], [2, 4]]),
    (1, 3, [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
    (2, 3, [[4, 6], [6, 9]]), 
    (1, 5, [[1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],
            [4, 8, 12, 16, 20],
            [5, 10, 15, 20, 25]]), 
])
def test_create_multiplication_table_logic(start_num, end_num, expected_table):

    actual_table = create_multiplication_table(start_num, end_num)
    assert actual_table == expected_table, \
        f"For start_num={start_num}, end_num={end_num}:\nExpected: {expected_table}\nActual: {actual_table}"

def test_script_output():
  
    expected_output = """[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

Formatted Table:
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
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