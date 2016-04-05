d = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

def prompt_user_for_city(d):
    city_guess = True
    while city_guess:
        current_city = input('Where are we beginning our journey?\n> ')
        if current_city in d.keys():
            return current_city
            city_guess = False

def append_to_visited_cities(current_city):
    visited_cities = []
    visited_cities.append(current_city)
    return visited_cities

def generate_next_city_list(d, current_city, visited_cities):
    next_stops = []
    for city in d[current_city]:
        if city not in visited_cities:
            next_stops.append(city)
    return next_stops

def prompt_user_for_next_city(next_stops, visited_cities):
    city_choice = True
    while city_choice:
        print(visited_cities)
        print('Available destinations', next_stops)
        current_city = input('Which city shall we travel to next?\n> ')
        if current_city in next_stop and current_city not in visited_cities:
            return current_city
            city_choice = False



current_city = prompt_user_for_city(d)
visited_cities = append_to_visited_cities(current_city)
next_stop = generate_next_city_list(d, current_city, visited_cities)

# second time

current_city = prompt_user_for_next_city(next_stop, visited_cities)

visited_cities = append_to_visited_cities(current_city)
next_stop = generate_next_city_list(d, current_city, visited_cities)
current_city = prompt_user_for_next_city(next_stop, visited_cities)





# # Practice: Road Trip
# In a faraway land, nearby cities are connected by roads.
# We've mapped what cities are directly connected by roads and stored them in a dict:
# ```python
# city_to_accessible_cities = {
#   'Boston': {'New York', 'Albany', 'Portland'},
#   'New York': {'Boston', 'Albany', 'Philadelphia'},
#   'Albany': {'Boston', 'New York', 'Portland'},
#   'Portland': {'Boston', 'Albany'},
#   'Philadelphia': {'New York'}
# }
# ```
# Traveling from one city to an adjacent one is called a **hop**.
# ​
# For this sort of problem, you'll want to iteratively visit cities you know you can access while updating:
# 1. Cities you can access.
# 1. Cities you've been to.
# 1. Cities you haven't been to.
# ​
# * Let the user enter a city.
# Print out all the cities connected to that city.
# * Let the user enter a city.
# Print out all cities that could be reached through two hops.
# ​
# ## Advanced
# * Let the user enter a city and a number of hops.
# Print out all cities that could be reached through that number of hops.
# * We've also mapped the travel time of each hop:
# ```python
# city_to_accessible_cities_with_travel_time = {
#   'Boston': {('New York', 4), ('Albany', 6), ('Portland', 3)},
#   'New York': {('Boston', 4), ('Albany', 5), ('Philadelphia', 9)},
#   'Albany': {('Boston', 6), ('New York',5), ('Portland', 7)},
#   'Portland': {('Boston', 3), ('Albany', 7)},
#   'Philadelphia': {('New York', 9)}
# }
# ```
# When the user enters a city and a number of hops, print out the shortest travel times to each city.
# Paths with fewer hops are not necessarily those with the shorter travel times.
