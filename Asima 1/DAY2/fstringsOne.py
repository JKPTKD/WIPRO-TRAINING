
id, name, sal = 1001, 'Raju Bhai', 125000.00
print(f'{id:5}{name:20}{sal:15.2f}') #default alignment
print(f'{id:<5}{name:<20}{sal:<15}') #Left aligned
print(f'{id:^5}{name:^20}{sal:^15}') #Center aligned 
print(f'{id:>5}{name:>20}{sal:>15}') #Right aligned
