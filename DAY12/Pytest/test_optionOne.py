import pytest
import subprocess
import sys
import os
from datetime import datetime, date 
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'optionOne.py')
def run_script_with_args(args_list):
    command = [sys.executable, SCRIPT_PATH] + args_list
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False 
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_no_arguments():
    stdout, stderr, returncode = run_script_with_args([])
    assert stdout == ""
    assert stderr == ""
    assert returncode == 0 

def test_list_option(monkeypatch):
    mock_system_output = "mocked_file1.txt\nmocked_file2.py"
    def mock_os_system(command):
        print(mock_system_output) 
        return 0 

    monkeypatch.setattr(os, 'system', mock_os_system)

    stdout, stderr, returncode = run_script_with_args(["-l"])
    expected_output = f"Listing files in current directory:\n{mock_system_output}"
    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0

    stdout, stderr, returncode = run_script_with_args(["--list"])
    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0


def test_date_option(monkeypatch):
    class MockDatetime:
        @classmethod
        def now(cls):
            return datetime(2025, 7, 21, 10, 30, 0) 

    monkeypatch.setattr('optionOne.datetime', MockDatetime) 

    stdout, stderr, returncode = run_script_with_args(["-d"])
    expected_date = "2025-07-21" 
    assert stdout == f"Today's date is: {expected_date}"
    assert stderr == ""
    assert returncode == 0

    stdout, stderr, returncode = run_script_with_args(["--date"])
    assert stdout == f"Today's date is: {expected_date}"
    assert stderr == ""
    assert returncode == 0


def test_echo_option():
    test_string = "Hello Pytest!"
    stdout, stderr, returncode = run_script_with_args(["-e", test_string])
    assert stdout == f"Echoed string: {test_string}"
    assert stderr == ""
    assert returncode == 0

    test_string_with_spaces = "Another string with spaces"
    stdout, stderr, returncode = run_script_with_args(["--echo", test_string_with_spaces])
    assert stdout == f"Echoed string: {test_string_with_spaces}"
    assert stderr == ""
    assert returncode == 0

def test_multiple_options(monkeypatch):
    mock_system_output = "test_files.txt"
    def mock_os_system(command):
        print(mock_system_output)
        return 0
    monkeypatch.setattr(os, 'system', mock_os_system)

    class MockDatetime:
        @classmethod
        def now(cls):
            return datetime(2025, 1, 15)
    monkeypatch.setattr('optionOne.datetime', MockDatetime)

    echo_string = "Combined Test"
    stdout, stderr, returncode = run_script_with_args(["-l", "-d", "-e", echo_string])

    expected_date = "2025-01-15"
    expected_output_lines = [
        "Listing files in current directory:",
        mock_system_output,
        f"Today's date is: {expected_date}",
        f"Echoed string: {echo_string}"
    ]
    expected_output = "\n".join(expected_output_lines)

    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0

def test_invalid_option():
    stdout, stderr, returncode = run_script_with_args(["-x"]) 
    assert "usage: optionOne.py" in stderr 
    assert "unrecognized arguments: -x" in stderr 
    assert returncode != 0
    assert stdout == ""

def test_missing_echo_value():
    """Test -e without providing a string."""
    stdout, stderr, returncode = run_script_with_args(["-e"])

    assert "usage: optionOne.py" in stderr
    assert "argument -e/--echo: expected one argument" in stderr
    assert returncode != 0
    assert stdout == ""