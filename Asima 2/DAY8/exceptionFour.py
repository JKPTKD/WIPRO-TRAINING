'''
    raising     
'''
def validInput():
    isValid, num = False , 0
    while not isValid:
        try:
            num = int(input('Enter a num(Non-Zero): ')) 
            if num == 0:
                raise ValueError('No zero Please')
        except:
            pass 
        else: 
            isValid = True
    return num

if __name__ =='__main__':
    num = validInput()
    print(f'Num accepted: {num}')

