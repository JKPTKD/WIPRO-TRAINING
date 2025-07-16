num = int(input("Enter a number: "))

if 11 <= num % 100 <= 13:
    suffix = "th"
else:
    suffix = "st" if num % 10 == 1 else "nd" if num % 10 == 2 else "rd" if num % 10 == 3 else "th"

print(f"{num}{suffix}")
