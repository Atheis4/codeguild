# The list, dictionary, and initial value of more_votes is set
votes = []
vote_totals = {}
more_votes = True

# The while loop continues to ask for votes until the user input's 'done'.
while more_votes:
    vote = input('Who would you like to vote for?\n> ')

    if vote == 'done':
        more_votes = False
    # Each vote is added (.append()) to the end of the list of votes.
    else:
        votes.append(vote)

# The for loop iterates (repeats over) the votes list (turned into a set to get rid of duplicates).
for candidate in set(votes):
    # Each unique name is assigned as a key in our dictionary and each value is set to the number of times (.count()) that name appears in our list of votes.
    vote_totals[candidate] = votes.count(candidate)

# Set winning_total to the highest value in our dictionary's 'list' of values.
winning_total = max(vote_totals.values())

# Print totals
print(vote_totals)

# Create a new view of the dictionary's key/value pairs. Repeat through the key/value pairs...
for k, v in vote_totals.items():
    # if there is a value equal to our winning total...
    if v == winning_total:
        print(k, 'wins the election with', str(winning_total), 'votes.')
