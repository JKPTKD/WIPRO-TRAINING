import myPkg.myModTwo as mt 
#import folder.file 
#import pkgName.moduleName

if __name__ == '__main__':
    print(f'dataOne: {mt.dataOne}')
    print(f'dataTwo: {mt.dataTwo}')

    mt.funOne()
    mt.funTwo()
    mt.funThree()
