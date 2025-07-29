#  DAY6 Q2
'''
Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
Date:19-July-2025
Purpose: recurrsive
'''
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)

# Example
num = 5
print("Factorial of", num, "is:", factorial(num))