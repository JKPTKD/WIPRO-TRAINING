import sys
if len(sys.argv) < 3:
    print("Insufficient arguments.")
    print("Usage: python voting.py <name> <age>")
else:
    name = sys.argv[1] 
    age = int(sys.argv[2])  

    if age >= 18:
        print(f"Hello '{name.capitalize()}', you are eligible to vote.")
    else:
        print(f"Hello '{name.capitalize()}', you are NOT eligible to vote.")
