#Creating Facotorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#Main Function
def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {factorial(num)}.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
