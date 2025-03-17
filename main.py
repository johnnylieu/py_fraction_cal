import sys
import re

# def parse_fraction(frac_str):
#     pattern = r'^(?:(?P<whole>\d+)(?:_(?P<numer>\d+)/(?P<denom>\d+))?|(?P<numerOnly>\d+)/(?P<denomOnly>\d+)|(?P<integer>\d+))$'
#     match = re.match(pattern, frac_str)

if len(sys.argv) > 1:
    operand = sys.argv[3]
    num1 = sys.argv[2]
    num2 = sys.argv[4]
    print(num1, operand, num2)

    if sys.argv[1] == "?":
        print("let's start")

        if operand == "+":
            print("add")
        
        elif operand == "-":
            print("minus")

        elif operand == r"\*":
            print("multiply")

        elif operand == "/":
            print("divide")

        else:
            print("Invalid operand.")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")

    else:
        print("Enter correct arguments.")

else:
    print("No command line arguments were provided.")