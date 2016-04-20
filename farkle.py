import random

def roll_dice(total_dice, rolls):
    while total_dice > 0:
        dice = random.randint(1, 6)
        rolls.append(dice)
        total_dice -= 1
        return rolls

def build_dict_of_rolls():
    for roll in rolls:
        roll_history[roll] = rolls.count(roll)
        return roll_history

def tally_points(score):
    for k, v in roll_history.items():
        if k == 1:
            if v >= 3:
                score += 1000 + (100 * (v - 3))
            else:
                score += 100 * v
        elif k == 5:
            if v >= 3:
                score += 500 + (50 * (v - 3))
            else:
                score += 50 * v
        else:
            if v >= 3:
                score += k * 100
    return score

# Initialize variables
rolls = [] # List
total_dice = 5 # Decrementing value for while loop - represents number of dice to roll.
points = 0
roll_history = {} # Dictionary

rolls = roll_dice(total_dice, rolls)
build_dict_of_rolls()
tally_points(points)


print(rolls)
print(roll_history)
print(total_dice)
print(points)

if points == 0:
    print('Farkle!')

re_rolls = []






# if __name__ == "__main__":
#     main()
