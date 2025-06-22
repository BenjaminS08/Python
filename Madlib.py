#Old MacDonald had a farm
#Ee i ee i o
#And on his farm he had some cows
#Ee i ee i oh
#With a moo-moo here
#And a moo-moo there
#Here a moo, there a moo
#Everywhere a moo-moo
#old MacDonald had a farm
#Ee i ee i o
#Old MacDonald had a farm
#Ee i ee i o
#And on his farm he had some chicks
#Ee i ee i o
#With a cluck-cluck here
#And a cluck-cluck there
#Here a cluck, there a cluck
#Everywhere a cluck-cluck
#Old MacDonald had a farm
#Ee i ee i o
def custom_song(name, animal, animal2, animal_sound1,animal_sound2, noun1,noun2, transition_word1, transition_word2, transition_word3, transition_word4):
    print("\n\n")
    print(f"{name} had a {noun1},")
    print(f"{transition_word1} {transition_word2} {transition_word3} {transition_word4}")
    print(f"And on His Farm He Had Some {animal}")
    print(f"{transition_word1} {transition_word2} {transition_word3} {transition_word4}")
    print(f"With a {animal_sound1} here")
    print(f"and a {animal_sound1} there")
    print(f"here a {animal_sound1} there a {animal_sound1}")
    print(f" Everywhere a {animal_sound1}")
    print(f"Old {name} had a {noun2}")
    print(f"And On his Farm, He had Some {animal2}")
    print(f"{transition_word1} {transition_word2} {transition_word3} {transition_word4}")
    print(f"With a {animal_sound2} here")
    print(f"And a {animal_sound2} there")
    print(f"here a {animal_sound2} there a {animal_sound2}")
    print(f"Everywhere a {animal_sound2}")
    print(f"{name} had a {noun2},")
    print(f"{transition_word1} {transition_word2} {transition_word3} {transition_word4}")
input_name = input("Enter a name: ")
input_animal = input("Enter an animals: ")
input_animal2 = input("Enter a animal: ")
input_noun1 = input("Enter a noun: ")
input_noun2 = input("Enter another noun: ")
input_animal_sound1 = input("Enter a Animal Sound")
input_animal_sound2 = input("Enter Another Animal Sound")
input_transition_world1 = input("Enter A Transition Word")
input_transition_world2 = input("Enter A Transition Word")
input_transition_world3 = input("Enter A Transition Word")
input_transition_world4 = input("Enter A Transition Word")

custom_song(name=input_name, animal=input_animal, animal2=input_animal2, noun1=input_noun1, noun2=input_noun2, animal_sound1=input_animal_sound1, animal_sound2 = input_animal_sound2, transition_word1 = input_transition_world1, transition_word2 = input_transition_world2, transition_word3 = input_transition_world3, transition_word4 = input_transition_world4)