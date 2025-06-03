current_age = int(input("What is your Age?")) #Recieves age input
if current_age >= 21:                         #Determines if they can Drink Alcohol Legally
    print("You can Buy Alcohol Legally")
else:
    print("You can not Buy Alcohol Legally")
if current_age >= 16:                         #Determines if they can Drive Legally
    print("You can Drive Legally")
else:
    print("You can not Drive Alcohol Legally")
if current_age >= 18:                         #Determines if they can Vote Legally
    print("You can Vote Legally")
else:
    print("You can not Vote Legally")
if current_age >= 65:                         #Determines if they can Recive a Senior Discount
    print("You can Recieve a Senior Discount")
else:
    print("You can not Recieve a Senior Discount")
print(f"You are {current_age} years old")
