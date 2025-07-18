'''
    findall will return a list
'''
 
import re
 
string ='Welcome to Regular expression. Today is 18-07-2025 having 1, 2 or more digits' #text or string
pattern = r'(\d{2})-(\d{2})-(\d{4})' #regex
 
print(f'{re.search(pattern, string)}')
res = re.search(pattern, string)
print (f'Res: {res}')
print (f'Res: {res.span()}')
print (f'Res: {res.group()}')
print (f'Res: {res.groups()}')
 
#print(f'{re.findall(pattern, string)}')