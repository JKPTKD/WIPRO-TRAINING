'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose:Creates a multiplication table from start_num to end_num as a list of lists.
'''
def create_multiplication_table(start_num, end_num):
    multiplication_table = []
    for i in range(start_num, end_num + 1):  
        row = []
        for j in range(start_num, end_num + 1):  
            row.append(i * j)
        multiplication_table.append(row)
    return multiplication_table
table = create_multiplication_table(1, 5)
print(table)
print("\nFormatted Table:")
for row in table:
    print(row)