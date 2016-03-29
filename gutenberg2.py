def open_file_text():
    """opens text file and saves as readlines"""
    with open('alice_in_wonderland.txt') as text_file:
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

def find_top_ten_words(single_word_dict):
    """rearranges key/value pair and saves to new sorted list"""
    count_to_word_pairs = [(v, k) for (k, v) in single_word_dict.items()]
    count_to_word_pairs_ascending_order = sorted(count_to_word_pairs, reverse=True)
    for k, v in count_to_word_pairs_ascending_order[:10]:
        print('The word \'{}\' appears {} times in this text.'.format(v, k))
    print()

def zip_word_list_pairs(word_list_stripped):
    word_pair_list = list(zip(word_list_stripped, word_list_stripped[1:]))
    return word_pair_list

def create_and_populate_word_pair_dict(word_pair_list):
    paired_word_dict = {}
    for x, y in word_pair_list:
        if x not in paired_word_dict:
            paired_word_dict[x] = {}
        if y not in paired_word_dict[x]:
            paired_word_dict[x][y] = 0
        paired_word_dict[x][y] += 1
    return paired_word_dict

def create_word_pair_count(paired_word_dict, word_pair_list):
    word_pair_count = []
    for x, y in word_pair_list:
        word_pair_count.append(paired_word_dict[x][y])
    return word_pair_count

def zip_count_to_word_pair_tuple(word_pair_list, word_pair_count):
    new_triplet = set(zip(word_pair_count, word_pair_list))
    return new_triplet

def sort_triplet_find_top_pairs(new_triplet):
    count_to_pairs_ascending_order = sorted(new_triplet, reverse=True)
    for k, v in count_to_pairs_ascending_order[:10]:
        print('The word pair {} appears {} times in this text.'.format(v, k))


text_file = open_file_text()
word_list_stripped = strip_text_to_list(text_file)
single_word_dict = create_dict_from_word_list_stripped(word_list_stripped)
find_top_ten_words(single_word_dict)

word_pair_list = zip_word_list_pairs(word_list_stripped)
paired_word_dict = create_and_populate_word_pair_dict(word_pair_list)
word_pair_count = create_word_pair_count(paired_word_dict, word_pair_list)
new_triplet = zip_count_to_word_pair_tuple(word_pair_list, word_pair_count)

count_to_pairs_ascending_order = sort_triplet_find_top_pairs(new_triplet)

# ADVANCED -----------------
