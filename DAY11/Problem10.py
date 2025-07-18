'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:18-July-2025
   Purpose: Primes start from 2, adjust start if it's less than 2.
'''
class PrimeGenerator:
    def __init__(self, start, count):
        if count < 0:
            raise ValueError("Number of primes (count) cannot be negative.")
        if start < 2:
            # Primes start from 2, adjust start if it's less than 2.
            self._current_num = 2
        else:
            self._current_num = start
        self._primes_found = 0
        self._target_count = count

    def __iter__(self):
        return self

    def _is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        if self._primes_found >= self._target_count:
            raise StopIteration

        while True:
            if self._is_prime(self._current_num):
                prime = self._current_num
                self._current_num += 1 # Move to the next number for the next check
                self._primes_found += 1
                return prime
            self._current_num += 1 # Not prime, check the next number

# --- Usage Example ---
if __name__ == "__main__":
    start_number = 100
    num_primes_to_find = 25

    print(f"Generating {num_primes_to_find} prime numbers starting from {start_number}:")
    prime_gen = PrimeGenerator(start=start_number, count=num_primes_to_find)

    # Iterate through the PrimeGenerator instance
    for prime in prime_gen:
        print(prime, end=' ')
    print() # For a new line after printing