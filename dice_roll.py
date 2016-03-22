import random

def get_number_of_dice_from_user():
    """Asks the user to input a number. This number represents the number of dice we are going to roll."""
    number_dice = int(input('How many dice would you like to roll?\n> '))
    return number_dice

def roll_dice(number_dice):
    """While the number of dice to roll is greater than zero, append a random integer from 1 to 6 onto our list of dice values, decrement number of dice, and return the dice values"""
    dice_values = []

    while number_dice > 0:
        dice_values.append(random.randint(1, 6))
        number_dice -= 1
    return dice_values

def count_total(dice_values):
    """Taking our individual rolls, we add the dice face value to our running total and return that value."""
    total = 0
    for dice in dice_values:
        total += dice
    return total

def mean_of_dice_rolls(total, number_dice):
    """Calculate the mean of our rolls by inputing the total and number of dice then dividing the two. Return the mean as the value of the function."""
    mean_of_dice = total / number_dice
    return mean_of_dice

def report_data_to_user(dice_values, total, mean_of_dice):
    """Report the scores to the user. Prints the number of rolls, the dice value list, the total score, and the mean value."""
    print('These are your {} rolls: {}'.format(len(dice_values), dice_values))
    print('They add together to equal {}.'.format(total))
    print('The mean value of your rolls is {}.'.format(mean_of_dice))


number_dice = get_number_of_dice_from_user()
dice_values = roll_dice(number_dice)
total = count_total(dice_values)
mean_of_dice = mean_of_dice_rolls(total, number_dice)
report_data_to_user(dice_values, total, mean_of_dice)
