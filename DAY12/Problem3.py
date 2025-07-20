#Remove empty strings
strings = ['hello', '', 'world', '', 'python']
filtered_strings = list(filter(lambda s: s != '', strings))
print(filtered_strings)