import random

day_temp = []

def prompt_user_for_days_of_weather():
    """Define the variable 'days_to_generate' as an integer from the input string prompting the user."""
    days_to_generate = int(input('How many days of weather?\n> '))
    return days_to_generate

def generate_temperatures(days_to_generate):
    """Using days_to_generate as a limiter, get random integers between 32 and 100 and save as the day_temp."""
    while days_to_generate > 0:
        day_temp.append(random.randint(32, 100))
        days_to_generate -= 1

def create_forcast_and_print(day_temp):
    for temp in day_temp:
        if temp > 90:
            forecast = 'HOT!'
        elif temp > 60:
            forecast = 'Nice!'
        else:
            forecast = 'Cold!'
        print(temp, forecast)

days_to_generate = prompt_user_for_days_of_weather()
generate_temperatures(days_to_generate)
create_forcast_and_print(day_temp)
