import subprocess

if __name__ == '__main__':
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString='__main__  printing from funFirst()'
    if resString in res.stdout:
        print('Expected REsult')
    else:
        print('NOT So Expected REsult')
    
    #assert resString in res.stdout