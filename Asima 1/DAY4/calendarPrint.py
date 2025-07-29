'''
dd = int(input('Enter the month: '))
yyyy = int(input('Enter the Year: '))
'''
dd, mm, yyyy = 1, 7, 2025
c, y = yyyy // 100, yyyy % 100

m = mm + 10 if mm <= 2 else mm - 2 #condition #1
y = y - 1 if m >= 11 else y  # condition #2

w = int(dd + (2.6 * m - 0.2) + y + y //4 + c // 4 - 2 * c ) % 7
months = ['January', 'February', 'March', 'April', 'May','June',
          'July','August','September','October','November', 'December']
print(f'   {months[mm-1]} {yyyy}')

print('Su Mo Tu We Th Fr Sa')
for _ in range(w):
    print(f'{" ":3}', end='')
for cnt in range(1,31):
    print(f'{cnt:<3}', end='')
    if (w + cnt) % 7 == 0:
        print()

