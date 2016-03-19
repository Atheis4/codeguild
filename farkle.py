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

for k, v in roll_history.items():
    if k == 1:
        if v >= 3 or v >= 4:
            points += 1000 + (100 * (v - 3))
        else:
            points += 100 * v
    elif k == 5:
        if v >= 3 or v >= 4:
            points += 500 + (50 * (v - 3))
        else:
            points += 50 * v
    else:
        if v >= 3:
            points += k * 100

print(roll_history)
print(points)

if points == 0:
    print('Farkle!')
