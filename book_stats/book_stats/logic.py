def open_file_text():
    """opens text file and saves as readlines"""
    with open('../alice_in_wonderland.txt') as text_file:
        text_file = text_file.readlines()
    return text_file

def strip_text_to_list(text_file):
    """normalizes text and saves to list of words"""
    text_file = ''.join(text_file).lower().split()
    punctuation = '?!.-,/\\()[]{}:;\n\'\"\t '
    word_list_stripped = [word.strip(punctuation) for word in text_file]
    return word_list_stripped

def create_dict_from_word_list_stripped(word_list_stripped):
    """Compiles dict, key = unique word, value = count total"""
    single_word_dict = {word: 0 for word in word_list_stripped}
    for word in word_list_stripped:
        single_word_dict[word] += 1
    return single_word_dict

def word_to_word_count(lookup):
    """input: word from user (lookup)"""
    global word_dict
    try:
        return word_dict[lookup]
    except KeyError:
        return 0

text = open_file_text()
word_list = strip_text_to_list(text)
word_dict = create_dict_from_word_list_stripped(word_list)
