'''
Problem #1:
-----------
print(' %-5s%-20s%-15s' % ('Id', 'Name', 'Sal'))
print(' %-5d%-20s%-15.2f' % (id, name, sal))

Problem #2:
-----------

id, name, sal = 1001, 'Raju Bhai', 125000.00
print('%s' % ('-' * 40))
print(' %-5s%-20s%-15s' % ('Id', 'Name', 'Sal'))
print('%s' % ('-' * 40))
print(' %-5d%-20s%-15.2f' % (id, name, sal))
print('%s' % ('-' * 40))
'''

id, name, sal = 1001, 'Raju Bhai', 125000.00
print(' %s' % ('-' * 48))
print('|  %-5s|  %-20s|  %-15s|' % ('Id', 'Name', 'Sal'))
print(' %s' % ('-' * 48))
print('|  %-5d|  %-20s|  %-15.2f|' % (id, name, sal))
print(' %s' % ('-' * 48))