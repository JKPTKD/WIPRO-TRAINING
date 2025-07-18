import re
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is?\s' #regex i 0 or 1 s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is{0,}\s' #regex i 0 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is*\s' #regex i 0 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is+\s' #regex i 1 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 