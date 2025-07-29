import re
string = 'Hello World\nHello is the word\nWorld is also a word'
pat = r'^Hello'
 
res = re.findall(pat, string, re.MULTILINE)
print(f'1. Res: {res}')
 
string = '''Hello World
Hello is the reword
World is also a matchword'''
pat = r'word$'
 
res = re.findall(pat, string, re.MULTILINE)
print(f'1. Res: {res}')
 