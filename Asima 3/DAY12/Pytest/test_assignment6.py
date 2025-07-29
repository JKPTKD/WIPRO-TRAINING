import subprocess
import sys
import os
import pytest
def run_palindrome_checker(input_string):

    script_path = os.path.join(os.path.dirname(__file__), 'Assignment6.py')

    try:
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_string + '\n')

        if process.returncode != 0:
            raise RuntimeError(f"Script exited with error code {process.returncode}\nStderr: {stderr}")

        return stdout.strip() 
                              

    except Exception as e:
        pytest.fail(f"Error running script: {e}")


def test_palindrome_simple():
    input_str = "madam"
    expected_output = "It is a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_palindrome_with_spaces_and_case():
    input_str = "Race car"
    expected_output = "It is a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_palindrome_sentence():
    input_str = "A man a plan a canal Panama"
    expected_output = "It is a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_not_palindrome_simple():
    input_str = "hello"
    expected_output = "It is not a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_not_palindrome_with_spaces():
    input_str = "Python test"
    expected_output = "It is not a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_empty_string():
    input_str = ""
    expected_output = "It is a palindrome" # "" == ""[::-1]
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"

def test_single_character_string():
    input_str = "a"
    expected_output = "It is a palindrome"
    actual_output = run_palindrome_checker(input_str)
    assert actual_output == expected_output, \
        f"For input '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"