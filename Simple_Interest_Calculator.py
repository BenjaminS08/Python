def calculate_interest(principal, rate, time):
    #Calculating interest 
    interest = (principal * rate * time) / 100
    return interest

def main():
    # Get input from the user and converts it to the appropriate types
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))

    # Calculates the interest
    interest = calculate_interest(principal, rate, time)

    # Prints the result 
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")

# Call the main function
main()
