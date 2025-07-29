''' 
    Name: Asima Nayak
    ID:30396
    Date: 4 July 2025
    Purpose: Toggle the bit pos on any given number
'''
num, pos = 10, 3
res = num ^ 1 << pos
print(f'after toggling {pos} bit on number {num} is {res}')