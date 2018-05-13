# This is the Number guesser file
import random
# Asks the user if they want to play
wantToPlay = input("Hello User! Would you like to play a number guessing game? Y or N: ")

while wantToPlay == "Y":
    # If yes, the game starts and a random number 1-100 is generated.
    guessed = False
    answer = random.randint(1, 101)

    while not guessed:
        # While the user has not guessed the number(the default state), the program continuously asks the user for a new
        # number and tells them if that is the correct number, higher than the number, or lower than the number
        print("I have my number, now you must guess it!")
        guess = int(input("Guess an integer between 1 and 100: "))
        if guess == answer:
            print("You guessed the number!")
            guessed = True
        if guess < answer:
            print("Too Low!")
        if guess > answer:
            print("Too High!")
            # asks the user if they would like to play again
    wantToPlay = input("Congrats on winning! Would you like to play again? Y or N: ")
print("Thanks for playing!")
