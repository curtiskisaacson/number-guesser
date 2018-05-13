#This is the Number guesser file
import random
wantToPlay = input("Hello User! Would you like to play a number game? Y or N: ")

while(wantToPlay =="Y"):
    guessed = False
    answer = random.randint(1,101)
    while(guessed == False):
        print("I have my number, now you must guess it!")
        guess = int(input("Guess an integer between 1 and 100: "))
        if guess==answer:
            print("You guessed the number!")
            guessed = True
        if guess<answer:
            print("Too Low!")
        if guess>answer:
            print("Too High!")
    wantToPlay = input("Congrats on winning! Would you like to play again? Y or N: ")