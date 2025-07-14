def main():
    print("Simple Addition and Subtraction Calculator")

    while True: #Not Sure how not to use while true in this scenario
        try:
            num1 = float(input("Enter the first number "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        op = input("Enter an operator (+ or -): ")
        if op in ['+', '-']:
            break
        else:
            print("Invalid operator. Please enter '+' or '-'.")

    while True:
        try:
            num2 = float(input("Enter the second number "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Perform the calculations
    if op == '+':
        result = num1 + num2
    else:  # op == '-'
        result = num1 - num2

    print(f"Result: {num1} {op} {num2} = {result}")
main()