def main():
    import calendar #importing required modules
    import datetime
    try:
        cyear = datetime.datetime.now().year #obtaining current year
        month = int(input("What month were you born?  "))
        if month <= 12 and month >=1: #validating input
            print(calendar.month(cyear,month)) #printing out the calendar
    

    except ValueError:
        print("Please enter a valid input")


main()
    