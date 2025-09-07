import random


# Task-1: Guess the number

# Generating  a random integer between 0 and 100 for computer guess .
computer_guess = random.randint(0, 100)

# Initialize a flag to control the game loop.
retry = True

# Start a loop that continues as long as 'retry' is True.
while retry:
    # Prompt the player to enter their guess and convert it to an integer.
    player_guess = int(input("Guess the number Between 1 to 100: "))

    # Check if the player's guess matches the computer's guess.
    if computer_guess == player_guess:
        print("Your Guess Is Correct")
        # If the guess is correct, set 'retry' to False to exit the loop.
        retry = False
    # If the player's guess is higher than the computer's guess.
    elif player_guess > computer_guess:
        print("Too high")
    # If the player's guess is lower than the computer's guess.
    elif player_guess < computer_guess:
        print("Too low")



# Task-2: Word Scramble

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Randomly select one word from the 'words' list.
random_word_selected = random.choice(words)

# Convert the selected word into a list of its individual characters.
convert_tolist = list(random_word_selected)

# Shuffle the order of characters in the list randomly.
random.shuffle(convert_tolist)

# Join the shuffled characters back into a string to create the scrambled word.
scrambled_word = "".join(convert_tolist)



# Initialize a boolean variable to control the game loop. 'True' means the game continues.
play_again = True


while play_again :
    # Display the scrambled word to the player and prompt them to guess.
    print("Your jumbled word is: " + scrambled_word)
    player_input = input("Guess the jumbled word  shown up here: ") # Get the player's input.

    # Check if the player's guess matches the originally selected word.
    if player_input == random_word_selected:
        print("Player Wins") # If they match, the player wins.
        play_again = False # Set 'play_again' to False to exit the loop.
    else:
        print("Try again") # If they don't match, inform the player to try again.
