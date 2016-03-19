# Advanced: Allow people to have multiple phone numbers and change the interface to allow adding multiple numbers and removing specific numbers.

phone_book = {}

def add_entry():
    more_entry = True

    while more_entry:
        name = input('What name would you like to enter? \n(Q to quit)\n> ')

        if name == 'Q'.lower() or name == 'QUIT'.lower():
            more_entry = False
            break
        else:
            phone_book[name] = input('What is their number? \n> ')

def lookup_entry():
    more_lookup = True

    while more_lookup:
        look_up = input('Whose number would you like to lookup? \n(Q to quit)\n> ')

        if look_up == 'Q'.lower() or look_up == 'QUIT'.lower():
            more_lookup = False
            break
        elif look_up in phone_book.keys():
            print('-' * 25)
            print(phone_book[look_up])
        else:
            print('I don\'t recognize that option.')

def change_entry():
    more_change = True

    while more_change:
        new_change = input('Who\'s entry would you like to change? \n(Q to quit)\n> ')

        if new_change == 'Q'.lower() or new_change == 'QUIT'.lower():
            more_change = False
        elif new_change in phone_book.keys():
            phone_book[new_change] = input('What is their updated number?:\n> ')
            print(new_change, '-', phone_book[new_change])
        else:
            print('I don\'t recognize that name.')

def phone_book_loop():
    not_done = True

    while not_done:
        print('-' * 25)
        print('Welcome to your Phonebook \n\nWhat would you like to do? \n1. Lookup Entries \n2. Add Entry \n3. Change Entry \n\nType QUIT to exit.')

        user_cmd = input('> ')

        if user_cmd == 'Q'.lower() or user_cmd == 'QUIT'.lower():
            not_done = False
        elif user_cmd == '1' or user_cmd == 'LOOKUP'.lower():
            lookup_entry()
        elif user_cmd == '2' or user_cmd == 'ADD'.lower():
            add_entry()
        elif user_cmd == '3' or user_cmd == 'CHANGE'.lower():
            change_entry()
        else:
            print('I don\'t recognize that command, please select an option. \n(1. Look up entry, 2. New entry, 3. Change entry, or Q to quit.)')

phone_book_loop()
