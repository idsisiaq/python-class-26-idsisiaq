# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS31
# Manav Patel
# 10/25/26
# Display message
print("=======================================")
print("      WELCOME TO COOKIE COMPANY!")
print("=======================================")

# User input if they want to continue
more_info = input("Would you like to learn more? (y/n): ").lower()

if more_info == "y" or more_info == "yes":
    print("\n --- The best cookies to exist ---")
    print("Our chocolate chip cookies are soft, sweet,")
    print("and filled with delicious chocolate chips.")
    print("They are perfect for sharing with friends")
    print("They are freshly baked and made with love.")
    print("Do you want to take a bite?")
    print("Get yours today for only $1.99 per cookie!")
    # User input to countinue
    purchase = input("\nWould you like to purchase a cookie? (y/n): ").lower()

    if purchase == "y" or purchase == "yes":
        # Customer information
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")

        # Calculations for the purchase
        price = 1.99
        quantity = int(input("Enter the quantity of cookies you want to purchase: "))
        subtotal = price * quantity
        tax = subtotal * 0.10
        total = subtotal + tax
        
        # Final output 
        print("\n===============================================")
        print("            COOKIE COMPANY RECEIPT")
        print("===============================================")
        print(f"Customer Name: {first_name} {last_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("-----------------------------")
        print("Product: Chocolate Chip Cookie")
        print(f"Quantity: {quantity}")
        print(f"Price per Cookie: ${price:.2f}")
        print("-----------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("===============================================")
        print("Thank you for your purchase! Enjoy your cookies!")
        print("Have a great day!\n")
    else:
        print("\nThanks for stopping by the Cookie Company!")
        print("Have a great day!\n")
else:
    print("\nThanks for stopping by the Cookie Company!")
    print("Have a great day!\n")