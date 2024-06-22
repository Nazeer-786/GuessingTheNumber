#Guess The Number Given by the computer.
# Explanation :  computer gives a secret number and guides us to find that secret number

import random

def guess_number(x) :
    rand_num = random.randint(1,x)
    guess = 0
    while guess!=rand_num :
        guess = int(input(f"Enter the guessing number between 1 and {x} : "))
        if guess < rand_num:
            print(f'sorry,Too Low. Enter greater than {guess} ')
        elif guess>rand_num:
            print(f'sorry,Too High. Enter smaller than {guess}')
    print(f'great! you found the secret number = {rand_num}')

#computer guesses the number you think.
def computer_guess(x):
    low  = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint(low,high)
        else :
            guess = low # low == high
        feedback = input(f'Is {guess}  Too High(H) or Too Low(L) or Is Correct (C) ??? : ')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess +1
    print(f'yay! computer guessed the number {guess}  Correctly')
computer_guess(10)
        
        
