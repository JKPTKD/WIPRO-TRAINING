import pytest
import subprocess
import os
import sys
import re 

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'loggingTwo.py')
LOG_FILE_NAME = 'testPrg.log'
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), LOG_FILE_NAME)


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """
    Fixture to ensure the log file is clean before and after each test.
    """
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)
    yield 
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)


def test_log_file_content():
    """
    Tests that loggingTwo.py correctly writes log messages to testPrg.log
    and that the script itself produces no stdout/stderr.
    """
    result = subprocess.run(
        [sys.executable, SCRIPT_PATH],
        capture_output=True,
        text=True,
        check=True 
    )


    assert result.stdout.strip() == "", f"Expected no stdout, but got: {result.stdout}"
    assert result.stderr.strip() == "", f"Expected no stderr, but got: {result.stderr}"

    assert os.path.exists(LOG_FILE_PATH), f"Log file '{LOG_FILE_NAME}' was not created."

    
    with open(LOG_FILE_PATH, 'r') as f:
        log_lines = f.readlines()

    expected_message_parts = [
        "-> DEBUG -> This is an debug level message\n",
        "-> INFO -> This is an Info level message\n",
        "-> WARNING -> This is an warning level message\n",
    ]
    assert len(log_lines) == len(expected_message_parts), \
        f"Expected {len(expected_message_parts)} log lines, but got {len(log_lines)}"
    log_line_pattern = re.compile(r'^\w{3} \w{3} \s*\d{1,2} \d{2}:\d{2}:\d{2} \d{4} (.*)$')
    for i, line in enumerate(log_lines):
        match = log_line_pattern.match(line)
        assert match is not None, f"Log line {i+1} format mismatch: '{line}'"
        actual_message_part = match.group(1)
        assert actual_message_part == expected_message_parts[i].strip(), \
            f"Log line {i+1} message mismatch.\nExpected part: '{expected_message_parts[i].strip()}'\nActual part: '{actual_message_part}'"

       