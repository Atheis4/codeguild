import random, sys

total_dice = 5
rolls_list = []

def roll_dice_add_to_list(total_dice, rolls_list):
    while total_dice > 0:
        dice_roll = random.randint(1, 6)
        rolls_list.append(dice_roll)
        total_dice -= 1
    return rolls_list

def generate_dict_from_rolls_list(rolls_list):
    roll_history_dict = {}
    roll_history_dict.clear()

    for roll in rolls_list:
        roll_history_dict[roll] = rolls_list.count(roll)
    return roll_history_dict

def calculate_score(roll_history_dict):
    points = 0

    for k, v in roll_history_dict.items():
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
                points += 100 * k
    return points

def check_for_farkle(points):
    if points == 0:
        print('Farkle')
        sys.exit()

def prompt_user_for_reroll(keep_rolling, points):
    re_roll = input('Would you like to reroll any dice? (Y/N)\n> ')

    if 'Nn' in re_roll:
        print('You have {} points. Thank\'s for playing.'.format(points))
        keep_rolling = False
    return keep_rolling

def return_dice_for_reroll(rolls_list):
    remove_dice = 0

    while remove_dice != 'done':
        print(rolls_list)
        remove_dice = input('Which dice would you like to reroll?\nType the dice number or \'done\' to continue.\n> ')
        remove_dice = int(remove_dice)
        rolls_list.remove(remove_dice)
        if remove_dice != int():
            print(rolls_list)

    print(rolls_list)
    return rolls_list



# def reroll_bool(points):
#     reroll_prompt = input('Would you like to reroll any dice? (Y/N)\n> ')
#     if reroll_prompt == 'n' or reroll_prompt == 'N':
#         print('You have {} points. Thank\'s for playing.'.format(points))
#         sys.exit()
#
# def return_dice_for_reroll(rolls_list):
#     while True:
#         try:
#             # When using, try to make 'try' blocks as short as possible.
#             print(rolls_list)
#             remove_dice = int(input('Which dice would you like to reroll.\nType the dice number or \'done\'\n> '))
#             rolls_list.remove(remove_dice)
#         except ValueError:
#             return rolls_list
#
#             # Don't use exceptions for control flow -- especially across function boundaries.
#             # input line - check to see if input is done -- if not done, then convert to int.

def add_reroll_to_total_dice(rolls_list):
    total_dice = 5 - len(rolls_list)
    return total_dice

def print_score(rolls_list, points):
    print('You have {} points'.format(points))
    print('Your current dice:', rolls_list)


keep_rolling = True
while keep_rolling:
    rolls_list = roll_dice_add_to_list(total_dice, rolls_list)
    roll_history_dict = generate_dict_from_rolls_list(rolls_list)
    points = calculate_score(roll_history_dict)
    print_score(rolls_list, points)
    check_for_farkle(points)
    prompt_user_for_reroll(keep_rolling, points)
    rolls_list = return_dice_for_reroll(rolls_list)
