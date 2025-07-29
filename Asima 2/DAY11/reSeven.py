'''
    finditer()
'''
import re
 
string = "Jan 1999, Feb 2005, Mar 2025"
for match in re.finditer(r"(\w{3}) (\d{4})", string):
    print(f"Month: {match.group(1)}, Year: {match.group(2)}")