def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    string = "Iterating through the string:"
    list_of_chars = list(string)
    print(list_of_chars)

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    text = "Character with the minimum ASCII value"
     
    print(min(text)) 

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    text2 = "Character with the maximum ASCII value:"
    print(max(text2))
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    word = "Python"
    print(word.index("o"))
    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    string2 = "Converting string to a list of characters:"
    list_of_chars2 = list(string2)
    print(list_of_chars2)
    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    sentence = "Count and print the number of occurrences of 'o' in the string"
    print(sentence.count("o")) 

main()