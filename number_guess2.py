import random

secret_number = random.randint(1, 10)

number_of_guesses = 3

print('Guess a number between 1 and 10. You only have 3 chances.')

while number_of_guesses > 0:
    guess = int(input('> '))
    if guess > secret_number:
        print('too high!')
    elif guess < secret_number:
        print('too low!')
    else:
        print('You got it!')
        break
