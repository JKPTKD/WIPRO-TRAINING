'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:11-July-2025
   Purpose: Capitalize First letter of each word in a string.
'''
text = input("Enter a string: ")
words = text.split()
capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
result = ' '.join(capitalized)
print("Output:", result)
