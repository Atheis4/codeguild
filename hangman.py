import random

word_list = 'cheese bacon aardvark ketchup pizza dope energy understand bool kitten storm python computer enough lame snare snark comment poo little speak easy mastodon quality quantify coffee beer weed scuba'.split()
total_guesses = 6
correct_letters = set()
incorrect_letters = set()

def get_secret_word(word_list):
    secret_word = random.choice(word_list)
    return secret_word

def get_user_guess(correct_letters, incorrect_letters):
    user_guess = input('Guess a letter:\n> ')

    if user_guess in correct_letters or user_guess in incorrect_letters:
        print('You\'ve already guessed that letter, guess again')
    elif len(user_guess) > 1:
        print('Type only one letter please.')

    return user_guess

def compare_user_guess(user_guess, secret_word):
    return user_guess in secret_word

def check_for_win(correct_letters, secret_word):
    return correct_letters == set(secret_word)

def ask_play_again():
    play_again = input('Would you like to play again? (Y/N)\n> ')
    return play_again

def display_game_board(secret_word, correct_letters, incorrect_letters):
    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    print(blanks)
    print('Your incorrect guesses: ', list(incorrect_letters))



secret_word = get_secret_word(word_list)

while total_guesses > 0:
    display_game_board(secret_word, correct_letters, incorrect_letters)

    user_guess = get_user_guess(correct_letters, incorrect_letters)

    if compare_user_guess(user_guess, secret_word):
        correct_letters.add(user_guess)
    else:
        incorrect_letters.add(user_guess)
        total_guesses -= 1

    if check_for_win(correct_letters, secret_word):
        print('You got it! The secret word was {}'.format(secret_word))
        play_again = ask_play_again()

        if play_again in 'yY':
            secret_word = get_secret_word(word_list)
            # total_guesses = 6
            # correct_letters = set()
            # incorrect_letters = set()
        else:
            print('Thank\'s for playing')

print('Sorry, the secret word was {}. Thank\'s for playing'.format(secret_word))
