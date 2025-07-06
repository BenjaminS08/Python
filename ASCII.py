def main():
    # Imputing a character
    user_input = input("Enter a single character: ")

    # Validating the input length
    if len(user_input) != 1:
        print("Please enter only one character.")
        return

    # Converting the character to ASCII value
    ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is {ascii_value}.")

    # ASCII value to character
    try:
        ascii_input = int(input("Enter an ASCII value (32–127): "))
        if 32 <= ascii_input <= 127:
            character = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is '{character}'.")
        else:
            print("Error: Please enter a value between 32 and 127.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
