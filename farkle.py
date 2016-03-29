# ADVANCED: Re-roll any dice, save scoring dice

import random

def roll_dice():
# Roll dice with randint, add rolls to list, decrement total_dice.
    while total_dice > 0:
        dice = random.randint(1, 6)
        rolls.append(dice)
        total_dice -= 1
        return rolls

def build_dict_of_rolls():
# For rolls in list, build dictionary 'roll_history': with key = dice value, value = occurance of dice value.
    for roll in rolls:
        roll_history[roll] = rolls.count(roll)
        return roll_history

def tally_points():
# Point tally
    for k, v in roll_history.items():
        if k == 1:
            if v >= 3:
                points += 1000 + (100 * (v - 3))
            else:
                points += 100 * v
        elif k == 5:
            if v >= 3:
                points += 500 + (50 * (v - 3))
            else:
                points += 50 * v
        else:
            if v >= 3:
                points += k * 100
    return points

# Initialize variables
rolls = [] # List
total_dice = 5 # Decrementing value for while loop - represents number of dice to roll.
points = 0
roll_history = {} # Dictionary

roll_dice()
build_dict_of_rolls()
tally_points()


print(rolls)
print(roll_history)
print(total_dice)
print(points)

if points == 0:
    print('Farkle!')

re_rolls = []


# else:
#     re_roll = input('Would you like to re-roll any dice? Y/N\n> ')
#
#     if re_roll == 'n' or re_roll == 'N':
#         print('You have {} points. Thank\'s for playing.'.format(points))
#     else:
#         return_dice = int(input('Which dice would you like to re-roll?\nType the dice value or \'done\'\n> '))
#
#         roll_history[return_dice] -= 1
#         rolls.remove(return_dice)
#         total_dice += 1
#
#         print(rolls)
#         print(roll_history)
#         print(total_dice)
#
# # roll_history[face] -= number_of_dice
#
# # print(roll_history)
