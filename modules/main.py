# main.py

from Mymathlib import basic, advanced
from Mymathlib.utilities import tools

print("Add: ", basic.add(10, 5))           # 15
print("Subtract: ", basic.subtract(10, 5)) # 5
print("Power: ", advanced.power(2, 3))     # 8
print("Factorial: ", advanced.factorial(5))# 120
print("Is Even: ", tools.is_even(4))       # True
