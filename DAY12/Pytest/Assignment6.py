# DAY5 Q2
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: Check for Palindrome.
'''
text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")