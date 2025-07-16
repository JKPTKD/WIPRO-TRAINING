import argparse
parser = argparse.ArgumentParser(description="Perform calculation on two numbers.")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("operator", type=str, help="Operator (+, -, *, /, %, //, **)")
parser.add_argument("num2", type=float, help="Second number")
args = parser.parse_args()
num1 = args.num1
operator = args.operator
num2 = args.num2
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
