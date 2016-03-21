def get_user_name_from_input():
    """" Prompt user for their name, return variable name, the string of the user's name"""
    name = input('What is your name?\n> ')
    return name

def print_greeting_with_user_name(name):
    """ Print the statement using the variable name from the previous function."""
    print('So nice to meet you, ' + name)

name = get_user_name_from_input()
print_greeting_with_user_name(name)
