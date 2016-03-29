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
    next_stop = []
    print('You are in', current_city)
    for city in d[current_city]:
        if city not in visited_cities:
            next_stop.append(city)
    return next_stop

def prompt_user_for_next_city(next_stop, visited_cities):
    city_choice = True
    while city_choice:
        print('Available destinations', next_stop)
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

print(visited_cities)
