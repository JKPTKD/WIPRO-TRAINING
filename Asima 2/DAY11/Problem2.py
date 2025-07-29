'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:18-July-2025
   Purpose:Find All Dates
'''
import re



def find_dates_with_groups(text):
    pattern = r"(\d{2})-(\d{2})-(\d{4})"
    return re.findall(pattern, text)

text_with_dates = "Today is 18-07-2025. My birthday is 01-01-1990. Another date: 31-12-2023. Invalid: 1-2-3"
dates_and_components = find_dates_with_groups(text_with_dates)
print(f"Text: '{text_with_dates}'")
print(f"Dates found with components (list of tuples): {dates_and_components}")
if dates_and_components:
    first_date_components = dates_and_components[0]
    print(f"First date: {first_date_components} (Day: {first_date_components[0]}, Month: {first_date_components[1]}, Year: {first_date_components[2]})")
print()
print("--- Problem #2: Find All Dates (Approach 2: re.finditer) ---")

def find_dates_iterative(text):
    pattern = r"\d{2}-\d{2}-\d{4}"
    dates = []
    for match in re.finditer(pattern, text):
        dates.append(match.group(0)) 
    return dates

dates_found_iter = find_dates_iterative(text_with_dates)
print(f"Text: '{text_with_dates}'")
print(f"Dates found using finditer: {dates_found_iter}")
print()