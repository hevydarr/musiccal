#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Guess the music genre! You can guess 3 times only.")
    print("..................................................")
    name = input("Enter your name:")
    print("\nWelcome," , name)

    music= [
        "jazz",
        "classic",
        "hiphop",
        "rap",
        "rock",
        "pop",
        "latin",
        "hindi"
        ]

    x = random.choice(music)
    guess = None
    
 
    
    for count in range (3):
        
        guess = str(input("\n What music am I thinking of? "))
        
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
    
    else:
        print("\n Sorry, you already tried 3 times. The correct music genre was:" , x)


main()

