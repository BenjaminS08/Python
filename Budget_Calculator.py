Total_Budget = float(input("What is your monthly income?")) #Asks for monthly Budget
print("Your Total Budget this month is: " , Total_Budget) #prints Total Budget For this month
Rent = float(input("What is your monthly rent?"))
Food = float(input("What is your monthly Spending on Food?"))
Utilities = float(input("What is your monthly amount Spent on Utilities?"))
Groceries = float(input("What is your monthly amount spent on Groceries?"))
Transportation = float(input("What is your monthly amount spent on transportation?"))
HealthCare = float(input("What is your monthly amount Spent on Health Care?"))
PersonalCare = float(input("What is your monthly amount Spent on Personal Care?"))
Ckothing = float(input("What is your monthly amount spent on clothing?"))
Debt = float(input("What is your monthly amount spent on Debt?"))
#Calculating Total Amout Spent this Month
Total_Spent = Rent + Food + Utilities + Groceries + Transportation + HealthCare + PersonalCare + Ckothing + Debt
print("Your Total Amount Spent This Month is: " , Total_Spent) #Prints Total Spent this month
#Calculating Total Budget Left 
Budget_Left = Total_Budget - Total_Spent
print("Your Total Budget Left this month is: " , Budget_Left) #Prints Budget Left this month
#Calculating Total Percent Spent on Each Category
Rent_Percentage = (Rent / Total_Budget) * 100
Food_Percentage = (Food / Total_Budget) * 100
Utilities_Percentage = (Utilities / Total_Budget) * 100
Groceries_Percentage = (Groceries / Total_Budget) * 100
Transportation_Percentage = (Transportation / Total_Budget) * 100
HealthCare_Percentage = (HealthCare / Total_Budget) * 100
PersonalCare_Percentage = (PersonalCare / Total_Budget) * 100
Clothing_Percentage = (Ckothing / Total_Budget) * 100
Debt_Percentage = (Debt / Total_Budget) * 100
print("Here are your Percentage Spent on each Category This Month, ")
print(f"Groceries {Groceries_Percentage}")
print(f"Rent {Rent_Percentage}")
print(f"Food {Food_Percentage}")
print(f"Utilities {Utilities_Percentage}")
print(f"Transportation {Transportation_Percentage}")
print(f"HealthCare {HealthCare_Percentage}")
print(f"PersonalCare {PersonalCare_Percentage}")
print(f"Clothing {Clothing_Percentage}")
print(f"Debt {Debt_Percentage}")
