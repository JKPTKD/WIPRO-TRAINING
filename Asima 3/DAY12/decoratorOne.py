def OuterFun(func):
    def InnerFun(arg):
        print(f'Before calling {func.__name__}({arg})')
        func(arg)
        print(f'After calling {func.__name__}({arg})')
        print('-' * 50)
    return InnerFun
@OuterFun
def funOne(num):
    print(f'funOne({num}) called')
@OuterFun 
def funTwo(num):
     print(f'funTwo({num}) called')
 
if __name__ == '__main__':
    funOne(100)
    funTwo('Some strings here')
 