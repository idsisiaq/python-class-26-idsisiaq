# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31
# Manav Patel
# 10/7/26

print("==================================== \n WELCOME TO THE MATH QUIZ \n====================================" )
# Collect user name and initialize variable
user = input("What is your Name: ")
score = 0
quiz_status = input(f"Hey {user} are you ready to take the quiz?(Y or N): ").upper()

# Validating user input 
while quiz_status != "N" and quiz_status != "NO" and quiz_status != "Y" and quiz_status != "YES":
    print(f"Hey {user} Please Enter a Valid Input (Y if Yes or N if No) \n")
    quiz_status = input(f"Hey {user} are you ready to take the quiz?(Y or N): ").upper()


if quiz_status == "Y" or quiz_status == "YES":
    print("\nAwnsers will have to be inputed in INTEGER form!\n")
    # Asking the user questions 
    print("***** Question 1 *****")
    question_1 = int(input("What is 5 + 5 = "))
    if question_1 == 10:
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
    print("\n***** Question 2 *****")
    question_2 = int(input("\nWhat is 5 x 5 = "))
    if question_2 == 25:
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
    print("\n***** Question 3 *****")
    
    question_3 = int(input("\nWhat is 5 / 5 = "))
    if question_3 == 1:
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
    print("\n***** Question 4 *****")
    
    question_4 = int(input("\nWhat is 5 - 5 = "))
    if question_4 == 0:
        score += 1 
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
    print("\n***** Question 5 *****")
    question_5 = int(input("\nWhat is 5 + 5(5) = "))
    
    if question_5 == 30:
        score += 1
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
    
    # Final Score output  
   
    if score == 5:
        print(f"\nCongratulations {user}! You got a perfect score of {score}!")
    elif score == 4:
        print(f"\nGood job {user} you almost got a perfect score! You got {score} out of 5 correct.")

    elif score == 3:
        print(f"\nGood attempt {user}! You got {score} out of 5 correct.")
    else:
        print(f"\nBetter Luck Next time {user}. You got {score} out of 5 correct. ")
    print("\n==================================== \n THANK YOU FOR TAKING THE QUIZ \n====================================" )

else:
    print(f"\nNo problem {user}! Come back when you are ready to take the quiz. \n")
    