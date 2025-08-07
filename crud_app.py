def main_menu(): #Menu Script
        print("Menu:")
        choice = 0
        while not(1 <= choice <= 5):
            try:
                print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
                print("1. Create a new entry")
                print("2. Display an entry by last name")
                print("3. Update an existing entry")
                print("4. Remove an entry")
                print("5. Quit")
                choice = int(input("Please enter the number of your selection: "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("That is not a valid number. Try again.")
            except ValueError:
                print("That is not a valid number. Try again.")
def main(): #Main script
    choice = 0
    while choice != 5:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
    print("\nData saved as customer_list.txt\n")

def read(): #Read Script
        try:
             
            customers = check()
            search_term = str(input(("Please Enter Last Name ")))
            for index, lines in enumerate(customers): #Used Enumerate python.org
             if search_term in lines:
                  print(lines)
                  return index, lines     
            print("Unable to Find Entry")
            return
        except Exception as e: #Error Excpetion handler
             print("An unexpected error occcured: {e}")    
             
       

def update(): #Update Script
        try:
            index,line = read()
            
            customers = check()
            customers.pop(index)
            fname = input("Please enter the customer\'s first name: ")
            lname = input("Please enter the customer\'s last name: ")
            phone = input("Please enter the customer\'s phone: ")
            email = input("Please enter the customer\'s email: ")
            entry = f"{fname}, {lname}, {phone}, {email} \n"
            print("Updating " + line + "to " + entry + "...\n")
            customers.append(entry)
            save(customers)
        except Exception as e:
             print("An unexpected error occcured: {e}")     

def delete(): #Delete Script
        index, line = read()
        #This will Return the Index and the Value
       
        customers = check()
        confirm = str(input("Are you sure you want to delete this? Y/N"))
        if confirm == "y":
            customers.pop(index)
        else:
             return
        save(customers)
        
        print("Deleting an entry...")
def check():
        try:
            print("Checking the system...")
    
            file = open("customer_list.txt", 'r')
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError: #Eoor Exception Handler
            print("Customer list does not exist. Creating a new file...")
            return []
def create(): #Create Script
        customer = check()
        fname = input("Please enter the customer\'s first name: ")
        lname = input("Please enter the customer\'s last name: ")
        phone = input("Please enter the customer\'s phone: ")
        email = input("Please enter the customer\'s email: ")
        entry = f"{fname}, {lname}, {phone}, {email} \n"
        customer.append(entry)
        print("Creating a new entry...")
        save(customer)

def save(output): #Save Script
        file = open("customer_list.txt", 'w')
        for line in output:
            file.write(line)
        file.close()
        print("File updated.")



main()