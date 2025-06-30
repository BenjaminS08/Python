# Simple Python program to calculate the square of a number with error handling

def square_number():
    try: #Tests to see if the input is a number or not
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Please enter a valid number.")

square_number()
