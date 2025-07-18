'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:18-July-2025
   Purpose:Finding Even numbers
'''
start, end = 1, 10
evenNumbers = (num for num in range(start, end + 1) if num % 2 == 0)

print("Even numbers using generator expression:")
for i in evenNumbers:
    print(i, end=' ')
print() 