poll_dict = {
    'chocolate': 0,
    'vanilla': 0,
    'strawberry': 0,
}

poll_dict_percentage = {
    'chocolate': 0,
    'vanilla': 0,
    'strawberry': 0,
}

def add_flavor(vote):
    if vote in poll_dict:
        poll_dict[vote] += 1

def get_mean_value_dict(total):
    print(total)
    for vote in poll_dict.keys():
        poll_dict_percentage[vote] = (poll_dict[vote] / total) * 100
    return poll_dict_percentage

def return_total():
    total = 0
    for value in poll_dict.values():
        total += value
    return total

def combine_pieces():
    total = return_total()
    poll_dict_percentage = get_mean_value_dict(total)
    return poll_dict_percentage
