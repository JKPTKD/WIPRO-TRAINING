try:
    #code that might raise an exception
    var = int(input('Enter a num: '))
    res = 100 / var 
    print(f'var is: {var}  and result: {res}')
except ZeroDivisionError:
    print(f'var(Denominator) cannot be 0.')     
except ValueError:     
    print(f'Invalid number input') 

    
