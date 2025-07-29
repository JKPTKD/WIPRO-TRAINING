var = None
try:
    var = int(input('Enter a num: '))
except ValueError:     
    var = 100
    print(f'Exception occured: so assigning value {var}')
else:
    pass
finally:
    print(f'var in binary: {var:b}  in octal: {var:o}')
    print(f'var in Dec: {var}  in Hexa: {var:x}')
