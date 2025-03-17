import sys

if len(sys.argv) > 1:
    operand = sys.argv[3]

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")

        if sys.argv[1] == "?":
            print("let's start")
            if operand == "+":
                print("add")
            
            elif operand == "-":
                print("minus")

            elif operand == "\*":
                print("multiply")

            elif operand == "/":
                print("divide")
            else:
                print("Invalid operand.")

        else:
            print("Enter correct arguments.")

else:
    print("No command line arguments were provided.")