import random


def main():
    random_number = random.randint(1, 100)
    guess = int(input("What number do you think it is?: "))
    while random_number != guess:
            difference = abs(random_number - guess)
            if difference <= 5:
                 
              print("Very Hot")
            elif difference <= 15:
                 print("Hot")
            elif difference <= 25:
                 print("Cool")
            elif difference > 25:
                 print("Cold")
            guess = int(input("What number do you think it is?: "))
    if random_number == guess:
         print("You Guessed the Number!")

            

main()




