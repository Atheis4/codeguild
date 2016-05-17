import random

def get_secret_number():
    secret_number = random.randint(1, 100)
    return secret_number

def prompt_user():
    user_guess = input('Guess a number between 1 and 100:\n> ')
    return user_guess

def check_guess_to_secret_number(secret_number, user_guess):
    while user_guess != secret_number:
        compare_guess_to_secret(secret_number, user_guess)
        prompt_user()
        
    if user_guess == secret_number:
        print('You win!')

def compare_guess_to_secret(secret_number, user_guess):
    if user_guess < secret_number:
        print('Too low')
    elif user_guess > secret_number:
        print('Too high')


secret_number = get_secret_number()
user_guess = prompt_user()
check_guess_to_secret_number(secret_number, user_guess)






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
