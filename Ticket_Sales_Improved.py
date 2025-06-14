original_seats = ["s1", "s2", "s3", "s4", "s5", "s6", "s7,", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15", "s16", "s16", "s17", "s18", "s19", "s20"]
available_seats = original_seats.copy()

print("Seats available:", available_seats)

while True:
    selected_seat = input("Choose a seat (or type '0' to quit): ")

    if selected_seat == "0":
        print("Seat selection ended.")
        break

    if selected_seat in available_seats:
        available_seats.remove(selected_seat)
        print(f"Seat {selected_seat} booked.")
    elif selected_seat in original_seats:
        print(f"Sorry, seat {selected_seat} is already taken.")
    else:
        print("That seat doesn't exist. Please choose a valid one.")

    if len(available_seats) == 0:
        print("All seats are booked. Thank you!")
        break
