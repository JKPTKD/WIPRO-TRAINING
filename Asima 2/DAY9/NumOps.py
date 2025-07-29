class NumOps:
    def __init__(self, num):  
        self.num = num

    def isEven(self):
        return self.num % 2 == 0

    def isPrime(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False
        return True

    def isArmstrong(self):
        num_str = str(self.num)
        power = len(num_str)
        total = sum(int(digit) ** power for digit in num_str)
        return self.num == total


if __name__ == '__main__':
    count = int(input("How many numbers do you want to check? "))
    
    for i in range(count):
        user_input = int(input(f"\nEnter number {i+1}: "))
        obj = NumOps(user_input)
        print(f"{user_input} --> Even: {obj.isEven()}")
        print(f"{user_input} --> Prime: {obj.isPrime()}")
        print(f"{user_input} --> Armstrong: {obj.isArmstrong()}")
