def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)

# Example
num = 5
print("Factorial of", num, "is:", factorial(num))
