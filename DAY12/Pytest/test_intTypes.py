import subprocess
import sys
import os

def test_int_types_output():
    script_path = os.path.join(os.path.dirname(__file__), 'intTypes.py')

    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().split('\n')
    assert output_lines[0] == 'value of var is 10'
    assert output_lines[1] == 'value of var is 0xa'
    assert output_lines[2] == 'value of var is 0o12'
    assert output_lines[3] == 'value of var is 0b1010'
    assert output_lines[4] == '----------------------------------'