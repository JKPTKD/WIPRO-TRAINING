'''
    formatted output using str.format() 
'''

id, name, sal = 1001, 'Raju Bhai', 125000.00
print('ID: {}\t\tName: {}\t\tSal: {}'.format(id, name, sal))
print('first: {}\t\tSecond: {}\t\tThird: {}'.format(id, name, sal))

print('first: {0}\t\tSecond: {1}\t\tThird: {2}'.format(id, name, sal))

print('first: {1}\t\tSecond: {0}\t\tThird: {2}'.format(id, name, sal))
print('first: {2}\t\tSecond: {1}\t\tThird: {0}'.format(id, name, sal))
print('first: {1}\t\tSecond: {2}\t\tThird: {0}'.format(id, name, sal))