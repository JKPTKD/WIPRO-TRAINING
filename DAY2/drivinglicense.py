age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible for Driving License")
elif age >= 45:
    print("Eligible for Driving License - Validity: 5 years")
elif age >= 35:
    print("Eligible for Driving License - Validity: 10 years")
else:
    print("Eligible for Driving License - Validity: 20 years")
