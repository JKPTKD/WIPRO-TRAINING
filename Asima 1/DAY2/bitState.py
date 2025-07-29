''' 
    Name: Asima Nayak
    ID:  30396
    Date: 4 July 2025
    Purpose: Check the state of bit pos on any given number
'''

num, pos = 10, 2
res = 'ON' if num & 1 << pos else 'OFF'
print(f'{pos} bit on number {num} is {res}')