'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose:Have a lengthy string.Print each character with its character count from the lengthy string
'''


text = "This is a sample string. This string is just a sample for counting each character."
text = text.lower()
char_count = {}
for char in text:
    if char != " ":  
        char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
    print(f"'{char}': {count}")
