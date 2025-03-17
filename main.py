import sys
import re

def parse_fraction(frac_str):
    # This pattern matches:
    # 1. Mixed numbers like "3_1/4"
    # 2. Simple fractions like "1/2"
    # 3. Whole numbers like "7"
    pattern = r'^(?:(?P<whole>\d+)(?:_(?P<numer>\d+)/(?P<denom>\d+))?|(?P<numerOnly>\d+)/(?P<denomOnly>\d+)|(?P<integer>\d+))$'
    match = re.match(pattern, frac_str)
    if match:
        if match.group("whole"):
            # Mixed number case
            whole = int(match.group("whole"))
            numer = int(match.group("numer"))
            denom = int(match.group("denom"))
            # Convert mixed number to improper fraction
            total_numer = whole * denom + numer
            return total_numer, denom
        elif match.group("numerOnly"):
            # Simple fraction case
            numer = int(match.group("numerOnly"))
            denom = int(match.group("denomOnly"))
            return numer, denom
        elif match.group("integer"):
            # Whole number case
            return int(match.group("integer")), 1
    else:
        raise ValueError("Invalid fraction format")

if len(sys.argv) > 1:
    operand = sys.argv[3]
    num1 = sys.argv[2]
    num2 = sys.argv[4]
    print(num1, operand, num2)

    fractions = [num1, num2]
    for frac in fractions:
        try:
            numer, denom = parse_fraction(frac)
            print(f"{frac} -> {numer}/{denom}")
        except ValueError as e:
            print(f"Error parsing {frac}: {e}")

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