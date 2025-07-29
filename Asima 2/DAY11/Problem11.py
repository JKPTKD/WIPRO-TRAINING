'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose: Initializes the FibonacciSeries generator.
'''
class FibonacciSeries:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Number of terms (n) cannot be negative.")
        self._n = n
        self._count = 0
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._count >= self._n:
            raise StopIteration

        if self._count == 0:
            self._count += 1
            return self._a # Yield the first term (0)
        elif self._count == 1:
            self._count += 1
            return self._b # Yield the second term (1)
        else:
            next_fib = self._a + self._b
            self._a = self._b
            self._b = next_fib
            self._count += 1
            return next_fib

# --- Usage Example ---
if __name__ == "__main__":
    num_fib_terms = 10

    print(f"Generating the first {num_fib_terms} Fibonacci numbers:")
    fib_gen = FibonacciSeries(n=num_fib_terms)

    for fib_num in fib_gen:
        print(fib_num, end=' ')
    print() # For a new line

    print("\nGenerating the first 5 Fibonacci numbers:")
    fib_gen_5 = FibonacciSeries(n=5)
    print(list(fib_gen_5)) # Convert to list to show all at once