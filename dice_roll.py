import random

print('How many di would you like to roll?')
num_di = int(input())
total_di = num_di
total = 0

while num_di > 0:
    dice_val = random.randint(1, 6)
    print(dice_val)
    total += dice_val
    num_di -= 1

print(total/total_di)
