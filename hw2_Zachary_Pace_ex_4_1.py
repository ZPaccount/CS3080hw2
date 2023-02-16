'''
Homework 2-4-1
Name: Zachary Pace
Date: 2/16/2023
Description: Guess Number Game
'''

import random

Done = False
tryNum = 0
number = random.randint(1, 20)
print("I am Thinking of a Number between 1 and 20. You have 10 tries.")

while Done is False:
    tryNum = tryNum + 1
    if tryNum < 10:
        guess = int(input("Guess the Number: "))
        if guess == number:
            Done = True
            Win = True
        elif guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
    else:
        Done = True
        Win = False

if Win is True:
    print("Good Job! You guessed the number in " + str(tryNum) + " Guesses!")
else:
    print("Sorry, the number was " + str(number))
