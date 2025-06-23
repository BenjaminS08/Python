# Global conversion constants
POUNDS_TO_Kilograms = 0.453592
INCHES_TO_Meters = 0.0254

def calculate_bmi(weight_pounds, height_inches):
       # Convert weight to kilograms
    weight_kg = weight_pounds * POUNDS_TO_Kilograms
    # Convert height to meters
    height_m = height_inches * INCHES_TO_Meters
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 25:
        category = "normal weight"
    elif 25 <= bmi < 30:
        category = "overweight"
    else:
        category = "obese"
    
    return bmi, category

def main():
       # Prompts the user for weight and height measurements
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    # Calls the BMI calculator function
    bmi_value, bmi_category = calculate_bmi(weight, height)
    
    # Display the result with 2 decimal places
    print(f"\nYour BMI is: {bmi_value:.2f}")
    print(f"You are in the {bmi_category} category.")

main()
