var=400
def OuterFun(arg):
    print(f'OuterFun({arg}) called having local{var}')
    var+=100
    def InnerFun():
        print(f'InnerFun()..arg:{arg} called -->{var}')
    InnerFun()
if __name__=='__main__':
    OuterFun(10)
    OuterFun('String here')
   