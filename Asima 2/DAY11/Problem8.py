'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose: A generator function that yields even numbers
    from 'start' to 'end' (inclusive of 'end').
'''
def evenGenerator(start, end):
    for num in range(start, end + 1): 
        if num % 2 == 0:
            yield num
start, end = 1, 10
print("Even numbers using generator function:")
evenNumbers = evenGenerator(start, end)

for i in evenNumbers:
    print(i, end=' ')
print() 