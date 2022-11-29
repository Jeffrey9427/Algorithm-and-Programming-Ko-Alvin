# pick a number from 1-100 
# take the user's input(int) and the program will tell if the user's guess is correct. 
# if the input is not correct, tell them if the guess was too high or too low.
# may use while loop, to let the program run until a guess is correct. 

import random
randomint = random.randint(1,100)
user_input = 0

while user_input != randomint:
    user_input = eval(input("Guess a number (1-100) : "))
    if user_input > randomint:
        print("Your guess is too high")
    elif user_input < randomint:
        print("Your guess is too low")
else:
    print("Nice! Your guessed it correctly")
