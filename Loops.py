# WHILE LOOP

'''
A while loop makes a section of code repeat until a certain condition is met. In this exercise, you will create a Python script that asks the user to correctly guess a number.
'''


'''

import random

print("Welcome to Guess the Number!")

print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False


# CREATING A WHILE LOOP

while isGuessRight != True:
          guess = input("Guess a number between 1 and 10: ")
          if int(guess) == number:
            print("You guessed {}. That is correct! You win!".format(guess))
            isGuessRight = True
          else:
            print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
            
            '''
            
'''
PSEUDOCODE

 1.  If the user has not guessed the correct answer, enter the loop.
    2.  Ask the user for a guess.
    3.  Is the guess the correct number?
    4.  If the correct guess, tell the user it was the correct guess and exit the loop.
    5.  If the wrong guess, tell the user it was the wrong guess and continue the loop.
    
'''

# FOR LOOP

print("Count to 10!")

for x in range (0, 11):
          print(x)
          