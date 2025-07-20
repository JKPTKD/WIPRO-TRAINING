import subprocess
import sys
import os
import pytest
def run_number_formatter(input_value):
    script_path = os.path.join(os.path.dirname(__file__), 'exceptionOne.py')

    try:
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=str(input_value) + '\n')
        return stdout.strip(), stderr.strip(), process.returncode
    except Exception as e:
        pytest.fail(f"Error running script process: {e}")

@pytest.mark.parametrize("input_num, expected_output", [
    (10, """var in binary: 1010 in octal: 12
var in Dec: 10 in Hexa: a"""),
    (0, """var in binary: 0 in octal: 0
var in Dec: 0 in Hexa: 0"""),
    (255, """var in binary: 11111111 in octal: 377
var in Dec: 255 in Hexa: ff"""),
    (-5, """var in binary: -101 in octal: -5
var in Dec: -5 in Hexa: -5"""), 
])
def test_valid_integer_input(input_num, expected_output):
    stdout, stderr, returncode = run_number_formatter(input_num)

    assert returncode == 0, f"Script exited with error code {returncode} for input {input_num}. Stderr: {stderr}"
    assert stderr == "", f"Script produced unexpected stderr for input {input_num}: {stderr}"
    assert stdout == expected_output, f"Output mismatch for input {input_num}.\nExpected:\n'{expected_output}'\nActual:\n'{stdout}'"

@pytest.mark.parametrize("invalid_input_str", [
    "abc",
    "4.5",
    " ",
    "", 
    "hello world",
])
def test_invalid_input_raises_value_error(invalid_input_str):
    stdout, stderr, returncode = run_number_formatter(invalid_input_str)
    assert returncode != 0, f"Script unexpectedly succeeded for invalid input '{invalid_input_str}'"
    assert "ValueError" in stderr, f"Expected ValueError in stderr for input '{invalid_input_str}', but got:\n{stderr}"
    assert "invalid literal for int()" in stderr, f"Expected specific ValueError message for input '{invalid_input_str}', but got:\n{stderr}"
    assert stdout == "", f"Unexpected stdout for invalid input '{invalid_input_str}': {stdout}"