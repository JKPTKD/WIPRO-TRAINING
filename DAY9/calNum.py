import sys

if len(sys.argv) < 4:
    print("Insufficient arguments")
    print("Usage: python calNum.py <num1> <operator> <num2>")
else:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '**':
        result = num1 ** num2
    else:
        result = "Invalid operator"

    print("Result:", result)
