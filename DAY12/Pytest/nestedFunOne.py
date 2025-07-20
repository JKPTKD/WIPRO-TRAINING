# DAY7 Q2
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: nested function 
'''
def Outer(oArg):
    print(f'In Outer({oArg})')
    def Inner(iArg):
        print(f'In Inner({iArg})')
        return iArg * 2

    print(f'coming out of Outer ({oArg}) --> {__name__}')
    return Inner(oArg + 10)

if __name__ == '__main__':
    print(f'Outer(20) --> returns {Outer(20)}')
    res = Outer(10)
    print(f'Outer(10) --> returns {res}')