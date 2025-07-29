#Check if Strings Start with a Vowel
strings_vowel_check = ['apple', 'banana', 'orange', 'grape', 'umbrella']
vowels = 'aeiouAEIOU'
vowel_starting_strings = list(filter(lambda s: s and s[0] in vowels, strings_vowel_check))
print(vowel_starting_strings)