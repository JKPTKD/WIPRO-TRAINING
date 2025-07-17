'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Private attributes
'''
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance #private attribute/data
   
    def deposit(self, amount):
        self.__balance += amount
 
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient balance!')
        else:
            self.__balance -= amount
 
    def getBalance(self):
        return self.__balance
 
if __name__ == '__main__':
    account = BankAccount(5000)#intial deposit
    print(f'Account Balance: {account.getBalance()}')
    account.deposit(10000)
    print(f'Account Balance: {account.getBalance()}')
    account.withdraw(15000)
    print(f'Account Balance: {account.getBalance()}')
    account.withdraw(5000)
    print(f'Account Balance: {account.getBalance()}')
 