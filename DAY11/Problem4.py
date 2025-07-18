'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:18-July-2025
   Purpose:Extract Capitalized Words
'''
import re
def extract_capitalized_words_basic(text):
    pattern = r"\b[A-Z][a-zA-Z]*\b"
    return re.findall(pattern, text)

text_for_capitalized_words = "Python is a Powerful Language. Regular Expressions are Useful. IBM and NASA are Acronyms."
capitalized_words_basic = extract_capitalized_words_basic(text_for_capitalized_words)
print(f"Text: '{text_for_capitalized_words}'")
print(f"Capitalized words (basic): {capitalized_words_basic}")
print()

def extract_capitalized_words_search_loop(text):
    pattern = r"\b[A-Z][a-zA-Z]*\b"
    words = []
    start_index = 0
    while True:
        match = re.search(pattern, text[start_index:])
        if match:
            words.append(match.group(0))
            start_index += match.end()
        else:
            break 
    return words

capitalized_words_loop = extract_capitalized_words_search_loop(text_for_capitalized_words)
print(f"Text: '{text_for_capitalized_words}'")
print(f"Capitalized words (search loop): {capitalized_words_loop}")
print()