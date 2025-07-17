class MyExceptionOne(Exception):
    'Object of this class is created for negative values'
    def __init__(self, val):
        self.value = val
        self.msg = f'Negative value {val} NOT Allowed'
        super().__init__(self.msg)
 
def mySqrt(num):
    if num < 0:
        raise MyExceptionOne(num)  
    return num ** 0.5
 
if __name__ == '__main__':
    try:
        res = mySqrt(100)
        print(f'Sqrt of 10 is {res}')
    except MyExceptionOne as e:
        print(f'Exception occurs: {e}')
   
 