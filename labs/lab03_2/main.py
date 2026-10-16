# Starting file for LAB 3-2
# Include your course number, student first and last name, and date in the comment header
# Cs31
# Manav Patel
# 10/15/26
# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")

# initialize variables
another_set = "y"

while another_set.lower() == "y":
    #initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    
    while True:
        

        
        test_score = input("Enter test score: ")
        
        if test_score.lower() == "end": #check if user wants to end input
            break
        else:
            test_score = int(test_score)      # Otherwise convert the input into int's

        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print(f"Test score must be from 0 through 100. "
              f"Score discarded. Try again.")

    # calculate average score
    if counter > 0:
        average_set = round(score_total / counter)
    else:
         average_set = 0               
   
    # format and display the result

    print("======================")
    print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_set}")
    print()
    another_set = input("Do you want to enter another set of scores? (y/n): ")
    print()

print("Bye!")

