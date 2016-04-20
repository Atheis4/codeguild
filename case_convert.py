def snake_to_camel(word):
    snake_split_list = word.split('_')
    camel_case_list = [word.capitalize() for word in snake_split_list]

    camel_case_final = ''
    for item in camel_case_list:
        camel_case_final += item

    return str(camel_case_final)


def camel_to_snake(word):
    word = word.replace('', ' ').split()
    letter_list = []
    for letter in word:
        if letter.isupper():
            letter = letter.lower().replace('', ' ').rstrip(' ')
        letter_list.append(letter)

    snake_word = ''
    for i in letter_list:
        snake_word += i

    return snake_word.lstrip().replace(' ', '_')

word = 'snake_case'


def normalize_to_list(word):
    hyphen = '-'
    underscore = '_'

    if hyphen in word:
        return word.lower().split(hyphen)
    elif underscore in word:
        return word.lower().split(underscore)
    else:
        word = word.replace('', ' ').split()
        letter_list = []
        for letter in word:
            if letter.isupper():
                letter = letter.lower().replace('', ' ').rstrip(' ')
            letter_list.append(letter)

        word = ''
        for i in letter_list:
            word += i
        return word.split()


def word_list_to_snake(word):
    return '_'.join(word)


def word_list_to_camel(word):
    camel_word = ''
    for i in word:
        camel_word += i.capitalize()
    return camel_word


def word_list_to_kebab(word):
    return '-'.join(word)


def word_list_to_constant(word):
    return '_'.join(word).upper()


def main():
    new_word = True

    while new_word:
        word_to_transform = input('\nEnter a variable name in snake_case, CamelCase, kebab-case, or CONSTANT_CASE:\n(enter \'done\' to quit program)\n> ')
        if word_to_transform == 'done':
            new_word = False
        else:
            word_list = normalize_to_list(word_to_transform)

            case_to_print = input('\nWhich case style would you like to transform your variable into?\n1. snake_case\n2. CamelCase\n3. kebab-case\n4. CONSTANT_CASE\n(enter \'done\' to quit program)\n> ')
            if case_to_print == 'done':
                new_word = False
            elif case_to_print == '1':
                print(word_list_to_snake(word_list))
            elif case_to_print == '2':
                print(word_list_to_camel(word_list))
            elif case_to_print == '3':
                print(word_list_to_kebab(word_list))
            elif case_to_print == '4':
                print(word_list_to_constant(word_list))
            else:
                print('not a valid command')

if __name__ == "__main__":
    main()