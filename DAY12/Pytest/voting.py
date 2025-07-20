# DAY9 Q2
'''
Name:Jyotisman Kirti Prakash
ID:31261
Email:jyotismankirtiprakash11@gmail.com
Date:19-July-2025
Purpose: voting
'''
import sys

if len(sys.argv) < 3:
    print("Insufficient arguments.")
    print("Usage: python voting.py <name> <age>")
else:
    name = sys.argv[1]
    try:
        age = int(sys.argv[2])
    except ValueError:
        print("Error: Age must be an integer.")
        sys.exit(1) 

    if age >= 18:
        print(f"Hello {name.capitalize()}, you are eligible to vote.")
    else:
        print(f"Hello {name.capitalize()}, you are NOT eligible to vote.")