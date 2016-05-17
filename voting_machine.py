"""
5-16-16:

Considering adding a main() and revising functions to better reflect IPO structure.
"""

vote_totals_dict = {}

def main():
    vote_list = []
    more_votes = True

    while more_votes:
        vote = input('Who would you like to vote for? (Type \'done\' to continue)\n> ')

        if vote == 'done':
            more_votes = False
        else:
            vote_list.append(vote)

    return vote_list

def create_dict_from_vote_list(vote_list):
    for candidate in set(vote_list):
        vote_totals_dict[candidate] = vote_list.count(candidate)
    return vote_totals_dict

def find_winning_vote_total(vote_totals_dict):
    winning_total = max(vote_totals_dict.values())
    return winning_total

def declare_winner_with_dict(vote_totals_dict, winning_total):
    print(vote_totals_dict)
    for k, v in vote_totals_dict.items():
        if v == winning_total:
            print(k, 'wins the election with', str(winning_total), 'votes.')


vote_list = main()
vote_totals_dict = create_dict_from_vote_list(vote_list)
winning_total = find_winning_vote_total(vote_totals_dict)

declare_winner_with_dict(vote_totals_dict, winning_total)
