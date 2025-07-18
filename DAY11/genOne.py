def genOne():
    print(f'1. statement')
    yield 1
    print(f'2. statement')
    yield 2
    print(f'3. statement')
    yield 3
    print(f'4. statement')
    yield 4
 
if __name__ =='__main__':
    res = genOne()
    '''
    print(f'1. res: {res}')
    resTemp = next(res)
    print(f'2. res: {resTemp}')
    resTemp = next(res)
    print(f'3. res: {resTemp}')
    resTemp = next(res)
    print(f'4. res: {resTemp}')
    resTemp = next(res)
    print(f'5. res: {resTemp}')
    resTemp = next(res)
    print(f'5. res: {resTemp}')
    '''
 
    for i in res:
        print(i)
 