lst = [
    ['Jim Jam Pops', 35.7],['Bourbon', 23.3],
    ['Krack Jack', 15.00],['Dark Fantasy', 12.0],
    ['Five Star', 20.0]
]
quantity = [4, 2, 6, 5, 3]
print(' %s' %('-' * 43))
print(f'| %-5s|%-13s|%-4s|%-6s|%-10s|' % ('SlNo', 'Name','Qty','Price','Amount'))
print(' %s' %('-' * 43))
total = 0.0
for i in range(len(quantity)):
    total += quantity[i]*lst[i][1]
    print(f'| { i+1:^5}|{lst[i][0]:<13}|{quantity[i]:^4}|{lst[i][1]:<6.2f}|{quantity[i]*lst[i][1]:10.2f}|')
print(' %s' %('-' * 43))
print(f'| %32s%10.2f|' % ('| Total|',total))
print(' %s' %('-' * 43))
