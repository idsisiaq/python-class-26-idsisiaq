# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header

def main():
    print("===========================================")
    print("     Welcome to the Story Generator!")
    print("===========================================")
    
    # Ask the user if they want to play the game
    play = input("Do you want to play? (y/n): ").lower()

    # Validate the user input
    while play != "y" and play != "n":
        print("Invalid input. Please enter y or n")
        play = input("Do you want to play? (y/n): ").lower()

    if play == "y":

        # Ask for the user's name & greet them
        name = input("What is your name? ")
        print()
        print(f"Hello, {name}! Let's get started creating stories.")

        stories_created = 0

        again = "y"
        
        while again == "y":
            print()
            print("Choose a story: ")
            print("a. The Haunted House")
            print("b. The Superhero Adventure")

            # Get the user's choice of story
            print()
            choice = input("Enter your choice (a/b): ").lower()

            # Validate the user input
            while choice != "a" and choice != "b":
                print("Invalid input. Please enter a or b")
                choice = input("Enter your choice (a/b): ").lower()

            if choice == "a":
                    # Get user input for the haunted house story
                adjective = input("Enter an adjective: ")
                animal = input("Enter an animal: ")
                food = input("Enter a type of food: ")
                verb = input("Enter a verb ending in -ing: ")
                place = input("Enter a place: ")
                number = input("Enter a number: ")

                    # Display the story 
                print(f""" 
One dark and stormy night, you walked into a {adjective} haunted house.
Suddenly, a {animal} jumped out from a corner and scared you!
You ran {number} steps and tripped over a pile of {food}.
While you were {verb}, you noticed a strange noise comeing from the basement.
You followed the sound and found a secret passage that led to a hidden {place}.
You decided to follow the passage and were never seen again. The end.
""")

            elif choice == "b":
                # Get user input for story 2
                superhero = input("Enter the name of a superhero: ")
                villain = input("Enter the name of a villain: ")
                verb = input("Enter a verb ending in -ing: ")
                adjective = input("Enter an adjective: ")
                object = input("Enter an object: ")
                number = input("Enter a number: ")
                name_for_movie = input("Enter a name for a movie: ")
                # Display the story
                print(f""" 
One morning, you teamed up with {superhero} to save the world.
Unfortunately, the evil {villain} appeared with a {adjective} plan.
Your only weapon was a giant {object}
you and {superhero} got chased for {number} miles while {verb} to escape the villain's clutches.
just as thing looked hopeless, you used the {object} to defeat the villain and save the day. 
The world cheered for you and {superhero} as you were hailed as heroes in the new blockbuster movie, "{name_for_movie}".
""")
            # Increment the number of stories created
            stories_created += 1

            # Ask the user if they want to create another story
            again = input("Do you want to create another story? (y/n): ").lower()

            # Validate the user input for play_again
            while again != "y" and again != "n":
                print("Invalid input. Please enter y or n")
                again = input("Do you want to create another story? (y/n): ").lower()
        print()
        print(f"Thanks for playing, {name}!")
        print(f"You created {stories_created} stories today. Goodbye!")
    else:
        print("Maybe next time!")


if __name__ == "__main__":
    main()

