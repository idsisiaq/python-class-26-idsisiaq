# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31
# Manav Patel
# 10/7/26

print("==================================== \n WELCOME TO THE MATH QUIZ \n ====================================" )

user = input("What is your Name: ")
score = 0
quiz_status = input(f"Hey {user} are you ready to take the quiz?(Y or N): ").upper()
if quiz_status != "N" or quiz_status != "NO":
    print(f"Come back when you're ready {user}!")

while quiz_status == "Y" or quiz_status == "YES":
    print("Awnsers will have to be inputed in INTEGER form")
    question_1 = int(input("What is 5 + 5 = "))
    if question_1 == 10:
        score += 1
    question_2 = int(input("What is 5 x 5 = "))
    if question_2 == 25:
        score += 1
    question_3 = float(input("What is 5 / 5 = "))
    if question_3 == 1:
        score += 1
    question_4 = int(input("What is 5 - 5 = "))
    if question_4 == 0:
        score += 1 
    question_5 = int(input("What is 5 + 5 + 5 = "))
    if question_5 == 15:
        score += 1
    # Score check
    if score == 5:
        print(f"Congratulations {user}! You got a perfect score of {score}!")
    elif score == 4:
        print(f"Good job {user}  you almost got a perfect score! You got {score} out of 5.")

    elif score == 3:
        print(f"Good try {user}! You got {score} out of 5.")
    else:
        print(f"Better Luck Next time {user}. You got {score} out of 5.")
    break;