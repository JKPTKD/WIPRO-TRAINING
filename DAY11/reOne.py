import re
 
string ='Welcome to Regular expression. Today is 18-07-2025' #text or string
pattern = r'\d{2}' #regex
 
if re.match(pattern, string):
    print('2 Digit Number found in string')
else:
    print('No 2 Digit number here')
 
print(f'{re.search(pattern, string)}')
print(f'{re.match(pattern, string)}')
 
 
 