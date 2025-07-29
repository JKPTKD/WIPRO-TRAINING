'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose: Accept a lengthy string:Fifty five crore thirty four lakhs twenty three thousand two hundred and sixty seven.
'''
def word_to_number(text):
    ones = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
    }

    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    multipliers = {
        "crore": 10000000,
        "lakhs": 1000000,
        "lakh": 100000,
        "thousand": 1000,
        "hundred": 100
    }

    words = text.lower().replace(" and", "").split()
    total = 0
    current = 0

    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in multipliers:
            current *= multipliers[word]
            total += current
            current = 0
        else:
            continue

    total += current
    return total
text = "fifty five crore thirty four lakhs twenty three thousand two hundred and sixty seven"
print(word_to_number(text))
