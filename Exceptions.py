# Custom exception class
class NotNumericError(Exception):
    def __init__(self, message="Input is not a numeric value."):
        super().__init__(message)


def get_numeric_input():
    while True:  # While true loop that loops until a valid input is entered
        try:
            user_input = input("Enter a number: ")

            if not user_input.isnumeric():
                raise NotNumericError(
                    "Error: You must enter a number.")

        except NotNumericError as e:
            print(e)  # Print custom error message

        else:
            print(f"You entered the number: {user_input}")
            break  # Exit loop if input is valid

        finally:
            print("End of input attempt.\n")


# Run the program
get_numeric_input()
