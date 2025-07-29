'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose:Replace Multiple Spaces 
'''
import re
def replace_multiple_spaces_direct(text):
    pattern = r"\s+"
    return re.sub(pattern, " ", text)

text_with_extra_spaces = "This   text  has    too many     spaces.\nAnd  some\tnewlines."
cleaned_text_direct = replace_multiple_spaces_direct(text_with_extra_spaces)
print(f"Original text: '{text_with_extra_spaces.replace('\n', '\\n').replace('\t', '\\t')}'") 
print(f"Cleaned text: '{cleaned_text_direct.replace('\n', '\\n').replace('\t', '\\t')}'")
print()
print("--- Problem #3: Replace Multiple Spaces (Approach 2: re.split and join) ---")

def replace_multiple_spaces_split_join(text):
    parts = re.split(r"\s+", text)
    return " ".join(filter(None, parts))

cleaned_text_split_join = replace_multiple_spaces_split_join(text_with_extra_spaces)
print(f"Original text: '{text_with_extra_spaces.replace('\n', '\\n').replace('\t', '\\t')}'")
print(f"Cleaned text (split/join): '{cleaned_text_split_join.replace('\n', '\\n').replace('\t', '\\t')}'")
print()