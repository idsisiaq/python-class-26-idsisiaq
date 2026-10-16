# Starting file for LAB 3-1
# Include your course number, student first and last name, and date in the comment header
# CS31
# Manav Patel
#10/15/26
# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
while True:
    # User Inputs
    miles_driven = float(input("Enter miles driven:  "))
    
    gallons_used = float(input("Enter gallons of gas used:  "))
    
    cost = float(input("Enter cost of gas per gallon: "))
    print()

    # Check for validation 
    if miles_driven> 0 and gallons_used > 0 and cost > 0:
        mpg = miles_driven / gallons_used
        total_cost = gallons_used * cost
        cost_per_mile = total_cost / miles_driven

        print(f"Miles Per Gallon: {mpg:.2f}")
        print(f"Total GasCost: ${total_cost:.2f}")
        print(f"Cost Per Mile: ${cost_per_mile:.2f}\n")
    else:
        print("Error: Please enter positive values for miles, gallons, and cost.")
    again_trip = input("Do you want to enter another trip? (y/n): ")

    if again_trip.lower() != 'y':
        break
print()
print("Bye!")
