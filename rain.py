import urllib.request
import statistics as stats

def import_web_data():
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as website:
        lines = [byte_line.decode('utf-8') for byte_line in website]
    return lines

def strip_split_slice_web_data(lines):
    new_line_list = [line.strip()[:17].split() for line in lines[11:]]
    return new_line_list

def get_rid_of_null_data_turn_numbers_to_int(new_line_list):
    """raw y data in hundreths of inches. Conversion happens in print functions"""
    x, y = list(zip(*new_line_list))
    y = ' '.join(y).replace('-', '0').split()
    rainfall_int_list = []
    for item in y:
        rainfall_int_list.append(float(item)*.01)
    date_to_rain_tuple = list(zip(x, rainfall_int_list))
    return date_to_rain_tuple
#
def create_dict_from_data_tuple(date_to_rain_tuple):
    rainfall_dict = {x: y for x, y in date_to_rain_tuple}
    return rainfall_dict

def print_single_day_with_most_rain(rainfall_dict):
    rainfall_to_date_tuple_ascending = sorted([(v, k) for (k, v) in rainfall_dict.items()], reverse=True)
    v, k = zip(*rainfall_to_date_tuple_ascending)
    print('The date with the most rainfall was {0} with\n{1:.2f} inches of rain.'.format(k[0], v[0]))

def create_year_to_rain_total_dict(rainfall_dict):
    year_to_rainfall_total_dict = {}
    for date in rainfall_dict.keys():
        year_to_rainfall_total_dict[date[-4:]] = 0

    for x, y in rainfall_dict.items():
        year_to_rainfall_total_dict[x[-4:]] += y

    return year_to_rainfall_total_dict

def print_year_with_most_rain(year_to_rainfall_total_dict):
    total_rain_to_year_tuple_ascending = sorted([(v, k) for (k, v) in year_to_rainfall_total_dict.items()], reverse=True)
    v, k = zip(*total_rain_to_year_tuple_ascending)
    print('The year with the most rain was {0} with\n{1:.2f} inches of rain.'.format(k[0], v[0]))

def create_avg_day_to_rain_total_dict(rainfall_dict):
    day_to_rainfall_total_dict = {}
    for date in rainfall_dict.keys():
        day_to_rainfall_total_dict[date[:-5]] = []

    for x, y in rainfall_dict.items():
        day_to_rainfall_total_dict[x[:-5]].append(y)

    return day_to_rainfall_total_dict

def print_date_with_most_rain_on_average(day_to_rainfall_total_dict):
    avg_rainfall_list = []
    for a, b in day_to_rainfall_total_dict.items():
        avg_rainfall_list.append(stats.mean(day_to_rainfall_total_dict[a]))
    most_rainfall = max(avg_rainfall_list)
    value_key_tuple = [(stats.mean(v), k) for (k, v) in day_to_rainfall_total_dict.items()]

    for v, k in value_key_tuple:
        if v == most_rainfall:
            print('The day with the most rain on average is {0} with\n{1:.2f} inches of rain.'.format(k, v))

def main():
    lines = import_web_data()
    new_line_list = strip_split_slice_web_data(lines)
    date_to_rain_tuple = get_rid_of_null_data_turn_numbers_to_int(new_line_list)
    rainfall_dict = create_dict_from_data_tuple(date_to_rain_tuple)
    print()
    print_single_day_with_most_rain(rainfall_dict)
    year_to_rainfall_total_dict = create_year_to_rain_total_dict(rainfall_dict)
    print()
    print_year_with_most_rain(year_to_rainfall_total_dict)
    day_to_rainfall_total_dict = create_avg_day_to_rain_total_dict(rainfall_dict)
    print()
    print_date_with_most_rain_on_average(day_to_rainfall_total_dict)


    user_choice = True

    while user_choice:
        print()
        date_lookup = input('Would you like to know the future\'s weather?\n(Enter date as DD-MMM, ex. 04-MAR -- type \'done\' to quit\n> ')
        if date_lookup in day_to_rainfall_total_dict.keys():
            print('If past is prologue: On {0} it might rain {1:.2f} inches.\nOr not.'.format(date_lookup, stats.mean(day_to_rainfall_total_dict[date_lookup])))
        if date_lookup == 'done':
            user_choice = False

main()
