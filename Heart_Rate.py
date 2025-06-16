
#Gather a user's heart rate (in BPM) for a day in a multi-level list
#Print the times and the heart rates on the screen
#Calculate and print the average heart rate


#Creating The Variables
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
total = 0

heart_rates = []

#obtaining information from user
for time in time_slots:
    bpm = float(input(f"Please enter your heart rate for {time}: "))
    bpm = round(bpm)

    while bpm < 40 or bpm > 180:
        confirm = input(
            f"The heart rate {bpm} BPM seems unusual, are you sure it's correct? (Y or N): ")
        if confirm.lower() == "y":
            break
        else:
            bpm = float(input(f"Please enter your heart rate for {time}: "))
            bpm = round(bpm)
    
    heart_rates.append([time, bpm])

#Print results to screen
for i in range(len(heart_rates)):
    print(f"For {heart_rates[i][0]}, the heart rate was {heart_rates[i][1]} BPM")
    total += heart_rates[i][1]

average = total / len(heart_rates)
print(f"\nYour average heart rate today was: {average:.1f} BPM")
