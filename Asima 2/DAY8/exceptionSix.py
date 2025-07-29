'''
    raising     
'''
def validInput():
    isValid, num = False , 0
    while not isValid:
        try:
            num / 0
            num = int(input('Enter a num(Non-Zero): ')) 
            if num == 0:
                raise ValueError('No zero Please')
        except ValueError as ve: # 
            print(f'Exception Occur: {ve}') 
        except Exception as e: #generic type
            print(f'Exception Type Occur: {e}')         
        else: 
            isValid = True
    return num

if __name__ =='__main__':
    num = validInput()
    print(f'Num accepted: {num}')

