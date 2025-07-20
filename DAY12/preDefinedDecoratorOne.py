from functools import lru_cache
@lru_cache(maxsize=8)
def fibo(num): #2 ^ n
    if num<=1:
        return num
    return fibo(num-1) + fibo(num-2)
 
 
def fiboCaller():
    from sys import argv
    if len(argv[1:]) == 0:
        num =10
    else:
        num = int(argv[1])
 
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')
 
 
if __name__=='__main__':
    fiboCaller()