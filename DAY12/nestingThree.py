def OuterFun(func):
    def InnerFun(arg):
        print(f'Before calling {func.__name__}({arg})')
        func(arg)
        print(f'After calling {func.__name__}({arg})')
        print('-' * 50)
    return InnerFun
 
def funOne(num):
    print(f'funOne({num}) called')
 
def funTwo(num):
     print(f'funTwo({num}) called')
 
if __name__ == '__main__':
    res = OuterFun(funOne) #InnerFun is returned and stored
    res(100) #This is InnerFun(100)
   
    resOne = OuterFun(funTwo)
    resOne('Some strings here')
 