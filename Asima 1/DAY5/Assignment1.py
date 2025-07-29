''' Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose:Have a lengthy string.Print each word with its word count from the lengthy string.
'''
text = "This is a sample string. This string is just a sample for counting each word and how many times each word appears in the string."

import string
for char in string.punctuation:
    text = text.replace(char, "")
text = text.lower()
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
