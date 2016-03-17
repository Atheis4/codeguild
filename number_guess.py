import random

secret_number = random.randint(1, 100)

guess = 0

print('Guess a number between 1 and 100:')

while guess != secret_number:
    guess = int(input('> '))

    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')

print('You got it!')







# import random
#
# secret_number = random.randint(1, 100)
#
# done = False
#
# while done == False:
#
#     print('Guess a number between 1 and 100.')
#     user_guess = int(input('> '))
#
#     if user_guess == secret_number:
#         print('You got it! Nice guess!')
#         done = True
#     elif user_guess < secret_number:
#         print('Your guess is too low.')
#     elif user_guess > secret_number:
#         print('Your guess is too high.')
