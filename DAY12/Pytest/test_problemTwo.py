import subprocess
import sys
import os
import re
import pytest

def test_day_of_week_calculation():
    script_path = os.path.join(os.path.dirname(__file__), 'problemTwo.py')

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True 
        )
        output = result.stdout.strip()
        print(f"Captured output: {output}")

        match = re.search(r"w value for (\d+)/(\d+)/(\d+) is (\d+)", output)

        assert match is not None, f"Output format mismatch: {output}"
        extracted_dd = int(match.group(1))
        extracted_mm = int(match.group(2))
        extracted_yyyy = int(match.group(3))
        calculated_w = int(match.group(4))
        expected_dd = 3
        expected_mm = 7
        expected_yyyy = 2025

        assert extracted_dd == expected_dd
        assert extracted_mm == expected_mm
        assert extracted_yyyy == expected_yyyy


        expected_w = 4 

        assert calculated_w == expected_w, \
            f"Expected w to be {expected_w}, but got {calculated_w} for {expected_dd}/{expected_mm}/{expected_yyyy}"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Script execution failed: {e.stderr}")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")