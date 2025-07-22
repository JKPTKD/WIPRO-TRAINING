import subprocess

def test_First():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString='__main__  printing from funFirst()'
    assert resString in res.stdout

def test_Second():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString='__main__'
    assert resString in res.stdout

def test_Third():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString='printing'
    assert resString in res.stdout