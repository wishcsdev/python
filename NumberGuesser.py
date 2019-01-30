import random

secret=str(random.randint(0,11))
def generator():
    print("Guess the number between 0 and 10")
    for numberOfGuesses in (0,4):
        guess=input()
        if guess==secret:
            print("Correct!")
            SystemExit()
        else:
            print("Incorrect, try again")
    print ("Correct number is," + secret)        
generator()

