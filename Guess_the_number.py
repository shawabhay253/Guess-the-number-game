# Guess the number(Computer)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print("Yay, congrats. You have guessed the number.")
# Guess the number(User)
# we can inverse the function above, we can come up with secret number and we can have the computer try to guess it. So now we are going to create a new function called computer guests.

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
# Basically we want to loop over this feedback expression.
    while feedback != 'c' and low != high:   # c=correct
        if low != high:
            guess = random.randint(low, high)
        else:                       
            guess = low # could also be high b/c low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower() 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")

computer_guess(10)
guess(10)  