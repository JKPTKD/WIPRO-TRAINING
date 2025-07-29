'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose:Initializes the EvenNumberGenerator.
'''
class EvenNumberGenerator:
    def __init__(self, start, end):
        self._current_num = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self._current_num <= self._end:
            if self._current_num % 2 == 0:
                even_num = self._current_num
                self._current_num += 1 
                return even_num
            self._current_num += 1 
        raise StopIteration
if __name__ == "__main__":
    start_range = 1
    end_range = 10

    print(f"Generating even numbers from {start_range} to {end_range}:")
    even_gen = EvenNumberGenerator(start=start_range, end=end_range)

    for even_num in even_gen:
        print(even_num, end=' ')
    print() 

    print("\nGenerating even numbers from 5 to 15:")
    even_gen_2 = EvenNumberGenerator(start=5, end=15)
    print(list(even_gen_2)) 