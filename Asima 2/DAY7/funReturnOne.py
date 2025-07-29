def isPrime(num):
    res = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            res = False
            break     
    return res

if __name__ == '__main__':
    #num = int(input('Enter a number: '))

    cnt, num= 0, 100
    while cnt < 25:
        if isPrime(num):
            print(num, end = ' ')
            cnt += 1
        num += 1