num = int(input("Enter a number: "))
def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == num

def is_factorial(num):
    if num < 1:
        return False
    fact = 1
    i = 1
    while fact < num:
        i += 1
        fact *= i
    return fact == num
def is_leap(num):
    return(num % 4 ==0 and num % 100 !=0) or (num % 400 ==0)
print("Is Even:", is_even(num))
print("Is Prime:", is_prime(num))
print("Is Palindrome:", is_palindrome(num))
print("Is Armstrong:", is_armstrong(num))
print("Is Factorial:", is_factorial(num))
print("Is Leap Year:",is_leap(num))
