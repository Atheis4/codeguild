# Roll 5 six-sided di
# Score all 5

#   3 x 1 = 1000
#   3 x 2 = 200
#   3 x 3 = 300
#   3 x 4 = 400
#   3 x 5 = 500
#   3 x 6 = 600
#       1 = 100
#       5 = 50

# ADVANCED: Re-roll any dice, save scoring dice

import random

rolls = []
total_dice = 5
points = 0

roll_history = {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while total_dice > 0:
    di = random.randint(1, 6)
    rolls.append(di)
    total_dice -= 1

for roll in rolls:
    roll_history[roll] = rolls.count(roll)

print(rolls)
print(roll_history)

for k, v in roll_history.items():

    if k == 1:
        if v >= 3:
            

print(points)

if points == 0:
    print('Farkle!')
