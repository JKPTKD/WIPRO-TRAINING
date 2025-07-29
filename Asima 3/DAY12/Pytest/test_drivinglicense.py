import subprocess
import sys
import os
import pytest
def run_driving_license_script(age):
    script_path = os.path.join(os.path.dirname(__file__), 'drivinglicense.py')

    try:
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,  
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True               
        )
        stdout, stderr = process.communicate(input=str(age) + '\n')

        if process.returncode != 0:
            raise RuntimeError(f"Script exited with error code {process.returncode}\nStderr: {stderr}")

        return stdout.strip()
    except Exception as e:
        pytest.fail(f"Error running script: {e}")

def test_age_below_18():
    age = 17
    expected_output = "Not eligible for Driving License"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_exactly_18():
    age = 18
    expected_output = "Eligible for Driving License - Validity: 20 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_between_18_and_34():
    age = 25
    expected_output = "Eligible for Driving License - Validity: 20 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_exactly_35():
    age = 35
    expected_output = "Eligible for Driving License - Validity: 10 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_between_35_and_44():
    age = 40
    expected_output = "Eligible for Driving License - Validity: 10 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_exactly_45():
    age = 45
    expected_output = "Eligible for Driving License - Validity: 5 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"

def test_age_above_45():
    age = 60
    expected_output = "Eligible for Driving License - Validity: 5 years"
    actual_output = run_driving_license_script(age)
    assert actual_output == expected_output, f"For age {age}, Expected: '{expected_output}', Got: '{actual_output}'"