'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose: Write a generator function myRange(start, end, step)
'''
def myRange_function_syntax(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be zero")

    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:  
        while current > end:
            yield current
            current += step
print("Problem #3b (myRange Generator - Function Syntax):")
mr_gen_b_pos = myRange_function_syntax(0, 10, 2)
print(list(mr_gen_b_pos))
mr_gen_b_default = myRange_function_syntax(1, 5)
print(list(mr_gen_b_default)) 
mr_gen_b_neg = myRange_function_syntax(10, 0, -1)
print(list(mr_gen_b_neg))
mr_gen_b_empty = myRange_function_syntax(5, 0)
print(list(mr_gen_b_empty)) 
mr_gen_b_empty_rev = myRange_function_syntax(0, 5, -1)
print(list(mr_gen_b_empty_rev))
print()