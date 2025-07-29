'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose: Check for Palindrome.
'''
text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
