# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(self, first_name, last_name, address, age, phone_number):
        self.__first_name = first_name  # Private variable for first name
        self.__last_name = last_name    # Private variable for last name
        self.__address = address    # Private variable for student ID
        self.__age = age             # Private variable for academic year
        self.__phone_number = phone_number
    # Method to get Person's info as a formatted string

    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"

    # Getter for first_name
    def get_first_name(self):
        return self.__first_name

    # Getter for last_name
    def get_last_name(self):
        return self.__last_name

    # Getter for address
    def get_address(self):
        return self.__address

    # Getter for year
    def get_age(self):
        return self.__age

    # Getter for Phone Number
    def get_phone_number(self):
        return self.__phone_number

    # Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Setter for studentID
    def set_address(self, address):
        self.__address = address

    # Setter for year
    def set_age(self, age):
        self.__age = age
    # Setter for Phone number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


def people():
    # Create the first Person instance
    person1 = Person("Alice", "Johnson", "123 Maple St", 30, "555-1234")

    # Create the second Person instance
    person2 = Person("Bob", "Smith", "456 Oak Ave", 42, "555-5678")

    # Printing their information
    print(person1.get_info())
    print(person2.get_info())


people()
