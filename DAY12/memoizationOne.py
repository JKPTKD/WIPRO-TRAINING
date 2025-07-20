result ={0:0,1:1}
def fibo(num):
    if num not in result:
        result[num] = fibo(num-1)+fibo(num-2)
    return result[num]
 
def fiboCaller():
    from sys import argv
    if len(argv[1:]) == 0:
        num=10
    else:
        num = int(argv[1])
 
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')
 
if __name__=='__main__':
    fiboCaller()