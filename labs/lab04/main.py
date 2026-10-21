# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# Manav Patel
# 10/21/26


import random





def display_title():
    print("==================================== \n WELCOME TO THE NUMBER GUESSING GAME \n====================================" )

def play_game():
    print("""  
        print
        E : Easy - Guess from 1 to 10, Limit 5 attempts
        M : Medium - Guess from 1 to 100, Limit 8 attempts
        H : Hard - Guess from 1 to 1000, Limit 10 attempts
        """)
    your_level = input("Choose a difficulty level (E, M, H): ").lower()
    if your_level == "e":
        limit = 10
        attempts = 5
    elif your_level == "m":
        limit = 100
        attempts = 8
    elif your_level == "h":
        limit = 1000
        attempts = 10
    else:
        print("Invalid input. Please choose a valid difficulty level.")
        return
    secret_number = random.randint(1, limit)
    print(f" I am thinking of a number form 1 to {limit}\n")
    count = 1 
    
    while (guess := int(input("What is your guess? "))) != secret_number and count < attempts:

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        count += 1

    if count == attempts:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")   
    else:
        print(f"Congratulations! You guessed the number in {count} tries!")

    



def main():
    display_title()
    name = input("What is your name: ")
    again = "y"
    while again.lower() == "y":
        difficulty = input("Choose a difficulty level (E, M, H): ").lower()
        play_game()

    again = input("Would you like to play again? (Y or N): \n")

    print(f"Thanks for playing {name}! Goodbye!")



if __name__ == "__main__":
    main()


