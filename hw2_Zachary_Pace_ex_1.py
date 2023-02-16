'''
Homework 2-1
Name: Zachary Pace
Date: 2/16/2023
Description: works through the Collatz Sequence
'''


def collatz(num):
    if num % 2 == 0:  # checks if even or odd
        new = num / 2
        print(str(num) + " / 2 = " + str(new))
    else:
        new = 3*num+1
        print("3 * " + str(num) + " + 1 = " + str(new))
    return new


value = int(input("Enter Number: "))  # gets input from user
while value != 1:  # iterates through sequence
    value = collatz(value)
