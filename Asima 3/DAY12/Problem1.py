import time
def timeIt(func):
    """
    A decorator that measures and prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper
@timeIt
def factorial(num):
    if num == 0:
        return 1
    else:
        res = 1
        for i in range(1, num + 1):
            res *= i
        return res
@timeIt
def fibo(num):

    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num + 1):
            a, b = b, a + b
        return b
print("--- Factorial Calculation ---")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 10: {factorial(10)}")
print(f"Factorial of 20: {factorial(20)}")

print("\n--- Fibonacci Calculation ---")
print(f"Fibonacci of 5: {fibo(5)}")
print(f"Fibonacci of 10: {fibo(10)}")
print(f"Fibonacci of 20: {fibo(20)}")
print(f"Fibonacci of 30: {fibo(30)}")