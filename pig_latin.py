def get_sentence_from_user():
    """sets the local variable sentence to the input given by user, returns this sentence as the value of the function"""
    user_sentence_str = input('Veni, vidi, vici! What would you like to translate?\n> ')
    return user_sentence_str

def split_sentence(user_sentence_str):
    """"sets the local variable to_be_translated to a list comprised of the words from our aforementioned sentence, returns this list for the function call."""
    pre_translated_list = user_sentence_str.split()
    return pre_translated_list

def translate_sentence_to_pig_latin(pre_translated_list):
    """Iterates through a lowercase version of the list of words to be translated and feeds it into the translation function"""
    post_translated_list = []

    for pre_translated_word in pre_translated_list:
        post_translated_list.append(translate_word_to_pig_latin(pre_translated_word))
    return post_translated_list

def translate_word_to_pig_latin(pre_translated_word):
    vowels = 'aeiouAEIOU'
    punctuation = '.?!,;:'
    pre_translated_word = pre_translated_word.lower()

    if pre_translated_word[0] in vowels and pre_translated_word[-1] in punctuation:
        pig_latin_word = ''.join(pre_translated_word[:-1] + 'yay' + pre_translated_word[-1])
    elif pre_translated_word[0] in vowels:
        pig_latin_word = ''.join(pre_translated_word + 'yay')
    elif pre_translated_word[-1] in punctuation:
        pig_latin_word = ''.join(pre_translated_word[1:-1] + pre_translated_word[0] + 'ay' + word[-1])
    else:
        pig_latin_word = ''.join(pre_translated_word[1:] + ''.join(pre_translated_word[:1].lower() + 'ay'))
    return pig_latin_word


def create_pig_latin_sentence(post_translated_list):
    """Takes the words from the list pig_sentence and adds them to a new string titled translated, returns this new string."""
    translated_sentence_str = ' '.join(post_translated_list)
    return translated_sentence_str

def print_pig_latin_sentence_str(translated_sentence_str):
    """Prints the final pig-latin sentence as a string."""
    print(translated_sentence_str)

user_sentence_str = get_sentence_from_user()
pre_translated_list = split_sentence_add_to_list(user_sentence_str)
post_translated_list = translate_sentence(pre_translated_list)
translated_sentence_str = create_pig_latin_sentence(post_translated_list)

print_pig_latin_sentence_str(translated_sentence_str)
