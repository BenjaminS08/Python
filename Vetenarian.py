class Pet:

    vet_name = "Happy Paws Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Private instances variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter methods
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    # Setter methods
    def set_owner_first_name(self, first_name):
        self.__owner_first_name = first_name

    def set_owner_last_name(self, last_name):
        self.__owner_last_name = last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # displaying pet and owner info
    def display_pet_info(self):
        print(f"Vet Name: {Pet.vet_name}")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print("-" * 40)


# checking if a property exists using hasattr
def check_property(obj, property_name):
    result = hasattr(obj, property_name)
    print(f"Does property '{property_name}' exist in object? {result}")


def main():
    # Creating three Pets
    pet1 = Pet("Alice", "Brown", 101, "Buddy")
    pet2 = Pet("John", "Doe", 102, "Whiskers", "Cat")
    pet3 = Pet("Maria", "Lopez", 103, "Goldie", "Fish")

    # Use setter method to change pet name for pet2
    pet2.set_pet_name("Shadow")

    # Displaying pet info for pet1 and pet2
    pet1.display_pet_info()
    pet2.display_pet_info()

    # Displaying info for all pets
    pet3.display_pet_info()

    # Checking if properties exist in pet objects
    check_property(pet1, "_Pet__pet_name")
    check_property(pet2, "pet_type")
    check_property(pet3, "_Pet__owner_email")


main()
