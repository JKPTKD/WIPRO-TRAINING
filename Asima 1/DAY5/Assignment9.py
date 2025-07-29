'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose: Check if string is pangram which consists of all characters (a-z) atleast one
'''
import string
text = input("Enter a sentence: ")
text = text.lower()
alphabet_set = set(string.ascii_lowercase)
text_set = set(text)
if alphabet_set.issubset(text_set):
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")
