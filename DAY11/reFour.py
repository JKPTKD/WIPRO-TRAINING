'''
    findall will return a list
'''
import re
 
string ='is this what you are lookig for. Is is is in it' #text or string
pattern = r'i.' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'(i.)' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'i[ins]' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'i[^ins]' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')