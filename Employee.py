# employee.py

# Base class: Employee
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


# Subclass: ProductionWorker
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_rate):
        super().__init__(name, number)
        self.__shift = shift  # 1 = Day, 2 = Night
        self.__hourly_rate = hourly_rate

    # Getters
    def get_shift(self):
        return self.__shift

    def get_hourly_rate(self):
        return self.__hourly_rate

    # Setters
    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

# main.py


def main():
    print("Enter Production Worker Details:")

    # Prompt for input
    name = input("Employee Name: ")
    number = input("Employee Number: ")

    while True:
        try:
            shift = int(input("Shift (1 for Day, 2 for Night): "))
            if shift in (1, 2):
                break
            else:
                print("Please enter 1 for Day or 2 for Night.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    while True:
        try:
            hourly_rate = float(input("Hourly Pay Rate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for hourly rate.")

    # Create ProductionWorker instance
    worker = ProductionWorker(name, number, shift, hourly_rate)

    # Display the stored information
    print("\nProduction Worker Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_rate():.2f}")


if __name__ == "__main__":
    main()
