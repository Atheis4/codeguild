import math


width = int(input('Enter the width of the wall in feet:\n> '))
height = int(input('Enter the height of the wall in feet:\n> '))
surface_area = width * height
coats_paint = int(input('How many coats of paint would you like to apply?\nPlease enter a whole number:\n> '))
paint_cost = float(input('How much does a gallon of paint cost?\n> '))


gal = math.ceil(surface_area / (coats_paint * 400))
total_cost = gal * paint_cost


print(surface_area, total_cost, gal, paint_cost)


dimension_tuple = (int(input('Enter room dimensions in feet: width, height\nHit <enter> to continue')))
print(dimension_tuple)
