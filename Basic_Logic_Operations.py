value1 = int(input("Input a Number?")) #integer  1 input #Recieves input for first number
value2 = int(input("Input a Number?")) #integer  2 input #Recieves input for second muber
if(value1 >0 and value2 >0): #checks if both values are greater than zero
    print("Both values are greater than zero")
else:(print("Both values are not greater than zero"))
if(value1 >100 and value2 >100): #checks if both values are greater than 100
    print("Both values are greater than 100")
else:(print("Both values are not greater than 100"))
if(value1 > value2 or value2 > value1): #checks if one of the values is greater than the other
    print("One of the Numbers is greater than the other")
else:(print("Both numbers are the same"))
if((value1%value2 == 0) or (value2%value1 == 0)): #checks if both numbers can be divided by each other
    print("One of the numbers if divisible by the other")
else:(print("Neither value is divisible by the other"))
if not value1 == value2: #checks if both numbers are equal
    print("Both Values are Equal")
else:print("Both Values are not equal")
if not value1%2 == 0: #checks if first number can be cleanly divided by two
    print("The first number cannot be divided by two into a whole number")
if not value2%2 == 0: #checks if second number can be cleanly divided by two
    print("The second number cannot be divided by two into a whole number")