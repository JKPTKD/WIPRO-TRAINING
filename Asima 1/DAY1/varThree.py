'''
    demo on variables
'''
var = 10
print(f'1. value of var is {var} @ {id(var)}') #format string

var = 10.234
print(f'2. value of var is {var}  @ {id(var)}')
#Triple quote
var = '''Some         
		string here 
		one multiple lines '''
print(f'3. value of var is "{var}"  @ {id(var)} ')