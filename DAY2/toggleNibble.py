''' 
    Name: Sudhakar Palanivelu
    ID:  
    Date: 4 July 2025
    Purpose: Toggle the nibble(combination of 4 bits) based 
    on the bit position on a given number
'''
num, pos = 10, 5
npos = pos // 4  # nibble position 
res = num ^ 0xf << npos * 4 # performing left shift on 15 (0b1111)
print(f'After toggling {npos} nibble number on {num} is {res}')