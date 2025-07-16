item = input("Enter item name: ")
price = float(input(f"Enter price of {item}: "))

print(f"{item} is cheap" if price < 100 else f"{item} is moderately priced" if price <= 500 else f"{item} is expensive")
