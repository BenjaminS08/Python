class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter methods
    def get_kind(self):
        return self.__kind

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    # Setter methods
    def set_kind(self, kind):
        self.__kind = kind

    def set_breed(self, breed):
        self.__breed = breed

    def set_name(self, name):
        self.__name = name

    # printing the pets details
    def print_details(self):
        print(f"Pet Name: {self.__name}")
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")
        print("-" * 30)


def main():
    # Three pet instances
    pet1 = Pet("Dog", "Labrador", "Buddy")
    pet2 = Pet("Cat", "Siamese", "Luna")
    pet3 = Pet("Bird", "Parrot", "Rio")

    # Printing the details of each et
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    # Special method demonstrations:
    print(f"Class name (__name__): {Pet.__name__}")
    print(f"Type of pet1: {type(pet1)}")
    print(f"Module where Pet is defined (__module__): {Pet.__module__}")


main()
