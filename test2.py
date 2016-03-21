import random

sum_list = []
sum_dict = {}
decrement = 5

while decrement > 0:
    num = random.randint(1, 6)
    sum_list.append(num)
    decrement -= 1

for poo in sum_list:
    sum_dict[poo] = sum_list.count(poo)

print('-' * 30)
print(sum_list)
print(sum_dict)

new_list = []
new_dec = 5
sum_dict.clear()

while new_dec > 0:
    lizard = random.randint(1, 6)
    new_list.append(lizard)
    new_dec -= 1

for nerd in new_list:
    sum_dict[nerd] = new_list.count(nerd)

print('-' * 30)

print(new_list)
print(sum_dict)
