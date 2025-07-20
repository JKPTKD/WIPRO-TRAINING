import subprocess
import sys
import os
import re
import pytest
def test_toggle_bit_calculation():
    script_path = os.path.join(os.path.dirname(__file__), 'toggleBit.py')

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True 
        )
        output = result.stdout.strip()
        print(f"Captured output: {output}") 
        match = re.search(r"after toggling (\d+) bit on number (\d+) is (\d+)", output)

        assert match is not None, f"Output format mismatch: {output}"
        extracted_pos = int(match.group(1))
        extracted_num = int(match.group(2))
        calculated_res = int(match.group(3))
        expected_num_script = 10
        expected_pos_script = 3

        assert extracted_num == expected_num_script
        assert extracted_pos == expected_pos_script

        expected_res = 2 

        assert calculated_res == expected_res, \
            f"Expected res to be {expected_res}, but got {calculated_res} for num={expected_num_script}, pos={expected_pos_script}"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Script execution failed: {e.stderr}")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")