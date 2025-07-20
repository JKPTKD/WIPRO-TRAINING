'''
Function Callback

'''
def funOne(func):
    print(f'Before call back')
    func()
    print(f'After call back')
    print('*' * 40)
    
def fun():
    print('fun() called')
    
def funTwo():
    print('funTwo() called')
if __name__=='__main__':
    funOne(fun)
    funOne(funTwo)