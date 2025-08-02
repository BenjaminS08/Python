def main():
    import calendar #importing required modules
    import datetime
    try:
        cyear = datetime.datetime.now().year #obtaining current year
        bmonth = int(input("What month were you born?  "))
        if bmonth <= 12 and bmonth >=1: #validating input
            print(calendar.month(cyear,bmonth)) #printing out the calendar
    

    except ValueError:
        print("Please enter a valid input")
    except:
        print("Something Went Wrong")

main()
    