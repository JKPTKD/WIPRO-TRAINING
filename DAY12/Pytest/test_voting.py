import pytest
import subprocess
import sys
import os

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'voting.py')

def run_script_with_args(args_list):

    command = [sys.executable, SCRIPT_PATH] + args_list
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False 
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_insufficient_arguments():
    stdout, stderr, returncode = run_script_with_args([])
    expected_output = "Insufficient arguments.\nUsage: python voting.py <name> <age>"
    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0 

    stdout, stderr, returncode = run_script_with_args(["John"])
    expected_output = "Insufficient arguments.\nUsage: python voting.py <name> <age>"
    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0

@pytest.mark.parametrize("name, age, expected_eligibility", [
    ("alice", 20, "eligible"),
    ("bob", 18, "eligible"),
    ("charlie", 17, "NOT eligible"),
    ("david", 5, "NOT eligible"),
    ("EVA", 30, "eligible"), 
])
def test_valid_age_eligibility(name, age, expected_eligibility):
    """Test with valid age inputs for eligibility."""
    stdout, stderr, returncode = run_script_with_args([name, str(age)])
    expected_output = f"Hello {name.capitalize()}, you are {expected_eligibility} to vote."
    assert stdout == expected_output
    assert stderr == ""
    assert returncode == 0

def test_invalid_age_non_integer():
    """Test when age is not an integer."""
    name = "frank"
    invalid_age = "twenty"
    stdout, stderr, returncode = run_script_with_args([name, invalid_age])
    assert stdout == "Error: Age must be an integer."
    assert stderr == "" 
    assert returncode == 1 

def test_invalid_age_float_string():
    """Test when age is a float string."""
    name = "grace"
    float_age = "18.5"
    stdout, stderr, returncode = run_script_with_args([name, float_age])
    assert stdout == "Error: Age must be an integer."
    assert stderr == ""
    assert returncode == 1

def test_empty_age_string():
    """Test when age is an empty string."""
    name = "helen"
    empty_age = ""
    stdout, stderr, returncode = run_script_with_args([name, empty_age])
    assert stdout == "Error: Age must be an integer."
    assert stderr == ""
    assert returncode == 1