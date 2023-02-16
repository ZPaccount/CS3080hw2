'''
Homework 2-4-3
Name: Zachary Pace
Date: 2/16/2023
Description: Guess Number Game, Random bounds, Plays itself
'''

import random

Done = False
tryNum = 0

upper = random.randint(1, 2000)  # Upper limit changed to 2000 so program has a decent chance to fail
lower = random.randint(1, upper-1)

number = random.randint(lower, upper)
print("I am Thinking of a Number between " + str(lower) + " and " + str(upper) + ". You have 10 tries.")

Win = False
lastGuess = -1
while Done is False:
    tryNum = tryNum + 1
    if tryNum < 10:
        guess = int((upper + lower) / 2)  # Guesses average of upper and lower
        if guess == lastGuess:
            guess = guess + 1
        lastGuess = guess
        print("Guess: " + str(guess))
        if guess == number:
            Done = True
            Win = True
        elif guess > number:
            print("Too High")
            upper = guess  # When guess is too high change upper
        elif guess < number:
            print("Too Low")
            lower = guess  # When guess is too low change lower
    else:
        Done = True
        Win = False

if Win is True:
    print("Good Job! You guessed the number in " + str(tryNum) + " Guesses!")
else:
    print("Sorry, the number was " + str(number))
