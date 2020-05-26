from random import randint
number_guess = randint(1, 50)
round = 3


for i in range(round):
    round -= 1
    user_guess = int(input(f'Round {i + 1} - Guess a number between 1 to 50: '))
    if user_guess == number_guess:
        print('You won !')
        break
    else:
        if user_guess > number_guess:
            print('You are too high !')
        else:
            print('You are too low !')
        if round != 0:
            print(f'You have {round} more guesses')
            print('Try again')
        else:
            print('Game over')

print(f'The guess number was {number_guess}')
            



