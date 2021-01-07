import random


def guess_game(x):
    random_number = random.randint(1, x)
    lives = 4
    guess = 0
    while guess != random_number and lives != 0:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Too low.')

            elif guess > random_number:
                print('Too high.')

            lives -= 1
            print(f'lives = {lives}')

            if lives == 0 & guess != random:
                print('sorry you died!')
                break

        except ValueError as err:
            print('Please enter a number ', err)
            continue

        if guess == random_number:
            print(f'Yay, congrats. you have guessed the number {random_number} correctly')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = None
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)

        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too Low (L), or correct (C)??'.lower())

        if feedback == 'h':
            high = guess - 1

        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number {guess}, correctly!')


guess_game(10)
# computer_guess(9)
