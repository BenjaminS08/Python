def main():
    #Initializing the list and counter
    books = []
    count = 0

    #Collecting 10 book titles using a while loop
    while count < 10:
        title = input(f"Enter book title #{count + 1}: ").strip()
        if title:  # Only add if input is not empty
            books.append(title.title())  # Capitalize properly
            count += 1
        else:
            print("Title cannot be empty. Please try again.")

    #Sorting the list alphabetically
    books_sorted = sorted(books)

    #Displaying each title from the sorted list
    print("\nSorted Book Titles:")
    for book in books_sorted:
        print(book)

main()
