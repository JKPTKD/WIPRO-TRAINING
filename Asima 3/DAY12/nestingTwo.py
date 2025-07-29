var = 400
def OuterFun(arg):
    print(f'OuterFun({arg}) called having')
    
    def InnerFun():
       global var
       print(f'InnerFun()..arg: {arg} called --> {var} ')
    InnerFun()
    
if __name__ == '__main__':
    OuterFun(10)
    OuterFun('String here')