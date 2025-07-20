#DAY7 Q1
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: fibonacci print
'''
def fiboPrint(num):
    def fibo(n):
        if n <= 1:
            return n
        return fibo(n-1) + fibo(n-2)

    for i in range(num):
        print(f'{i+1}: {fibo(i)}')
    print(f'\n------------------ {__name__}--------------------------')

print(f'module name --> {__name__}')

if __name__ == '__main__':
    #num = int(input('Enter the num: ')) # Commented out in screenshot
    fiboPrint(20)