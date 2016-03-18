votes = []
vote_totals = {}

more_votes = True

while more_votes:
    print('For whom would you like to vote?')
    vote = input()

    if vote == 'done':
        more_votes = False
    else:
        votes.append(vote)

for candidate in set(votes):
    vote_totals[candidate] = votes.count(candidate)

winner_votes = max(vote_totals.values())

print(vote_totals)

for k, v in vote_totals.items():
    if winner_votes == v:
        print(k, 'wins the election with', str(winner_votes), 'votes.')
