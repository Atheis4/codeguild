import random

# def logic()
# # def logic(rolls, roll_history, total_dice, points):
# #     points = 0
# #     while total_dice > 0:
# #         dice_roll = random.randint(1, 6)
# #         rolls.append(dice_roll)
# #         total_dice -= 1
# #
# #     for roll in rolls:
# #         roll_history[roll] = rolls.count(roll)
# #
# #     for k, v in roll_history.items():
# #         if k == 1:
# #             if v >= 3 or v >= 4:
# #                 points += 1000 + (100 * (v - 3))
# #             else:
# #                 points += 100 * v
# #         elif k == 1:
# #             if v >=  3 or v >= 4:
# #                 points += 500 + (50 * (v - 3))
# #             else:
# #                 points += 50 * v
# #         else:
# #             if v >= 3:
# #                 points += 100 * k
# #
# #     print(rolls)
# #     print(roll_history)
# #     print(points)
# #     print('-' * 30)

rolls = []
roll_history = {}
total_dice = 5
points = 0

# logic(rolls, roll_history, total_dice, points)
while total_dice > 0:
    dice_roll = random.randint(1, 6)
    rolls.append(dice_roll)
    total_dice -= 1

for roll in rolls:
    roll_history[roll] = rolls.count(roll)

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
            points += 100 * k

print()
print('Your rolls:', rolls)
print('Your points:', points)
print('-' * 30)
# End of logic()

if points != 0:
    re_roll = input('Would you like to reroll any dice?\nY/N?\n> ')

    if re_roll == 'N' or re_roll == 'n':
        print('You have {} points. Thank\'s for playing.'.format(points))
    else:
        while True:
            try:
                print('-' * 30)
                print('Your current roll:', rolls)
                print()
                return_dice = int(input('Which dice would you like to return?\n(Type the dice number or \'re-roll\' to continue)\n> '))
                rolls.remove(return_dice)
            except ValueError:
                break

        total_dice = 5 - len(rolls)
        roll_history.clear()
        points = 0

        # logic(rolls, roll_history, total_dice, points)
        while total_dice > 0:
            dice_roll = random.randint(1, 6)
            rolls.append(dice_roll)
            total_dice -= 1

        for roll in rolls:
            roll_history[roll] = rolls.count(roll)

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
                    points += 100 * k

        print('-' * 30)
        print('Your rolls:', rolls)
        print('You have {} points:'.format(points))
        print()
        print('Thank\'s for playing.')
        print('-' * 30)
        # End of logic()
else:
    print('Farkle! Thank\'s for playing.')
