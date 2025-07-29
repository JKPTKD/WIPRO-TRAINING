'''
    Apply the formula mentioned in the algorithm. 
    The result w  will be 0-6 in integer value 
    where 0 --> sun, 1 --> mon, 2 --> tue .... 6 --> sat

    yyyy = 2025
    y --> 25 last two digits of yyyy --> yyyy % 100
    c --> 20 i.e., firt 2 digits of yyyy ---> yyyy // 100
'''
dd, mm, yyyy = 3, 7, 2025
c, y = yyyy // 100, yyyy % 100

m = mm + 10 if mm <= 2 else mm - 2 #condition #1
y = y - 1 if m >= 11 else y  # condition #2

w = int(dd + (2.6 * m - 0.2) + y + y //4 + c // 4 - 2 * c ) % 7
print(f'w value for {dd}/{mm}/{yyyy} is {w}')
