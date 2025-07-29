'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose:Replace Digits with * 
'''
import re
def replace_digits_with_asterisk_direct(text):
    pattern = r"\d"
    return re.sub(pattern, "*", text)
text_with_digits = "Product ID: 12345. Price: $99.99. Date: 2025-07-18."
transformed_text_direct = replace_digits_with_asterisk_direct(text_with_digits)
print(f"Original text: '{text_with_digits}'")
print(f"Transformed text (direct sub): '{transformed_text_direct}'")
print()
def replace_digits_with_custom_char(text, char_map):
    pattern = r"\d"
    return re.sub(pattern, lambda m: char_map.get(m.group(0), '*'), text)
custom_map = {'1': 'A', '2': 'B', '3': 'C'}
transformed_text_custom = replace_digits_with_custom_char(text_with_digits, custom_map)
print(f"Original text: '{text_with_digits}'")
print(f"Transformed text (custom map): '{transformed_text_custom}'")
def replace_digits_with_asterisk_lambda(text):
    pattern = r"\d"
    return re.sub(pattern, lambda m: '*', text) 
transformed_text_lambda = replace_digits_with_asterisk_lambda(text_with_digits)
print(f"Transformed text (lambda to '*'): '{transformed_text_lambda}'")
print()