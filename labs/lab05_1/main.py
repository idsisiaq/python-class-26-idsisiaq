# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# Manav Patel CS31 10/28/26
import nameformat 


def main():
    # Program Title
    print("Welcome to the Name Format Module program")
    print()

    # Ask for first/last name
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    

    # Menu System
    while True:
        print(" * * MENU * *")
        print("1 - Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - Read Module Documentation")
        print("5 - Exit Program")

        menuChoice = input("What would you like to do? ")

        # if else block based on user choice

        if menuChoice == "1":
            # Call sayHello
            nameformat.sayHello(firstName)
        elif menuChoice == "2":
            # Call fullName
            nameformat.fullName(firstName, lastName)
        elif menuChoice == "3":
            # Call LastNameFirst
            nameformat.lastNameFirst(firstName, lastName)
        elif menuChoice == "4":
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)
            
        elif menuChoice == "5":
            print("Thank you for trying nameformat.")
            break;
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()