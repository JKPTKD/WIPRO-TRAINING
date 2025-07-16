import argparse
parser = argparse.ArgumentParser(description="Perform basic arithmetic operations.")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("operator", choices=["+", "-", "*", "/", "//", "%", "**"], help="Operator (+, -, *, /, //, %, **)")
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
elif operator == '//':
    result = num1 // num2
elif operator == '%':
    result = num1 % num2
elif operator == '**':
    result = num1 ** num2
print("Result:", result)
