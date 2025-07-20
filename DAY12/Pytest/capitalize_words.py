#DAY5 Q1
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: capitalize words
'''
def capitalize_words(text):
    words = text.split()
    capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized)

if __name__ == "__main__":
    text = input("Enter a string: ")
    result = capitalize_words(text)
    print("Output:", result)
