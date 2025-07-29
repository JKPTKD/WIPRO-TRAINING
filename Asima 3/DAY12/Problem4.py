#Find the max string by length
strings_for_max = ['apple', 'banana', 'orange', 'grape']
longest_string = max(strings_for_max, key=lambda s: len(s))
print(longest_string)