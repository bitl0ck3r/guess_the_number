import random

x = int(input('select range: '))


def guess(x):
    random_number = random.randint(1, x)
    lives = 4
    guess = 0
    while guess != random_number and lives != 0:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

        lives -= 1
        print(f'lives = {lives}')

        if lives == 0 & guess != random_number:
            print('Sorry you died!')
            break

    if guess == random_number:
        print(f'Yay, congrats. you have guessed the number {random_number} correctly!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
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

    print(f'Yay! The computer guessed you number {guess}, correctly!')


guess(x)
# computer_guess(x)
