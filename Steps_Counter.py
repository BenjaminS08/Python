#Creating Two separate Lists days and Steps
days = ["Mondays", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = []
#for loop with user input
for days in days:
    steps.append(int(input(f"How many steps did you take on {days}?")))
#printing how many steps on each day
for i in range(len(days)):
    steps = steps[i]
    next_day = days[i]
    print(f"You took {steps} steps on {next_day}.")
#calculating and printing total steps
total_steps = 0
for s in steps:
    total_steps += s
print("Total Steps: {total_steps}")
average_steps = total_steps // 7
print(f"Average Steps: {average_steps}")