import statistics

list_for_dict = 'this is a string of text it will be entered into a dictionary and the words will be counted i need to think of things to add to this text the more it has the better it will be as a representation of a sample size to extract statistical information from what else should i talk about this is harder than it looks stream of consciousness typing i was also trying to watch a game of star craft how many more words should i type he should know that this game is over he has four bases agains two the terran has no economy and mules are not nearly that good ok there it goes game over ladies and gentleman is this enough text to be fussing with my back and shoulder is really bugging me i think i could easily argue for a medical marijuana card jesus the pain'.split()

d = {}

for x in list_for_dict:
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] += 1

print(d)

for x in d.keys():
    print(statistics.mean(d.values()))
