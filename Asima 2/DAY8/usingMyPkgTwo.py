import myPkg
#import myPkg.myModTwo as mt 
if __name__ == '__main__':
    print(f'dataOne: {myPkg.dataOne}')
    print(f'dataTwo: {myPkg.dataTwo}')

    myPkg.funOne()#myPkg.myModTwo.funOne()
    myPkg.funTwo() #os.path.join()
    myPkg.funThree()

    print(f'Add: {myPkg.add(10,20)}')
    print(f'Sub: {myPkg.sub(10,20)}')
    print(f'Modi: {myPkg.modi(10,20)}')
    print(f'Modf: {myPkg.modf(109,100)}')
