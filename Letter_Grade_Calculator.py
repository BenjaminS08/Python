number_grade = int(input("what number Grade did you recieve?  ")) #gains user input on the number grade they recieved 
if number_grade < 60:
    letter_grade = "F" #If the grade is below 60 they have an F
elif number_grade <= 69:
    letter_grade = "D"
elif number_grade <= 79:
    letter_grade = "C"
elif number_grade <= 89:
    letter_grade = "B"
elif number_grade <= 100:
    letter_grade = "A"
print(f"You got a {letter_grade}")