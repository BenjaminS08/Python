def modify_artist_list(artist_list):
    try:
        index = int(input("Enter the index (0-9) of the artist you want to replace: "))
        new_artist = input("Enter the new artist's name: ")
        artist_list[index] = new_artist
        print(f"Updated list:\n{artist_list}")
    except (ValueError, IndexError):
        print("An input error occurred.")

def main():
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Elvis Presley",
        "Mariah Carey", "Stevie Wonder", "Janet Jackson",
        "Michael Jackson", "Whitney Houston", "Rihanna"
    ]
    
    print("Top 10 Performing Artists of All Time:")
    for i, artist in enumerate(top_artists):
        print(f"{i}: {artist}")
    
    modify_artist_list(top_artists)

main()
