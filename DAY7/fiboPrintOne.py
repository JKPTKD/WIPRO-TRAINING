def fiboPrint(num):
    def fibo(n):
        if n<=1:
            return n 
        return fibo(n-1) + fibo(n-2)

    for i in range(num):
        print(f'{i+1}:  {fibo(i)}')
    print(f'\n---------{__name__}------------------------')    

print(f'module name --> {__name__}')

if __name__ == '__main__':
    #num = int(input('Enter the num: '))
    fiboPrint(20)
