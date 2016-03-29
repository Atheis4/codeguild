import urllib.request

def import_web_data():
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as website:
        lines = [byte_line.decode('utf-8') for byte_line in website]
    return lines

def strip_split_slice_web_data(lines):
    new_line_list = [line.strip()[:17].split() for line in lines[11:]]
    return new_line_list

def get_rid_of_null_data_turn_numbers_to_int(new_line_list):
    day_month_year_list, y = list(zip(*new_line_list))
    y = ' '.join(y).replace('-', '0').split()
    rainfall_int_list = []
    for item in y:
        rainfall_int_list.append(int(item))
    return day_month_year_list, rainfall_int_list

def unzip_then_zip_data_for_tuple(day_month_year_list, rainfall_int_list):
    data_list_tuple = list(zip(day_month_year_list, rainfall_int_list))
    return data_list_tuple

def create_dict_from_data_tuple(data_list_tuple):
    rainfall_dict = {x: y for x, y in data_list_tuple}
    return rainfall_dict

def print_single_day_with_most_rain(rainfall_dict):
    rainfall_to_date_tuple_ascending = sorted([(v, k) for (k, v) in rainfall_dict.items()], reverse=True)
    v, k = zip(*rainfall_to_date_tuple_ascending)
    print('The date with the most rainfall was', k[0], '\nwith', (v[0] * .01), 'inches of rain.')

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
    print('The year with the most rain was', k[0], '\nwith', (v[0] * .01), 'inches of rain.')

def create_avg_day_to_rain_total_dict(rainfall_dict):
    day_to_rainfall_total_dict = {}
    number_of_each_date_in_data = {}
    for date in rainfall_dict.keys():
        day_to_rainfall_total_dict[date[:-5]] = 0
        number_of_each_date_in_data[date[:-5]] = 0

    for x, y in rainfall_dict.items():
        day_to_rainfall_total_dict[x[:-5]] += y
        number_of_each_date_in_data[x[:-5]] += 1

    for x, y in number_of_each_date_in_data.items():
        if x in day_to_rainfall_total_dict.keys():
            day_to_rainfall_total_dict[x] /= y

    return day_to_rainfall_total_dict

def print_date_with_most_rain_on_average(day_to_rainfall_total_dict):
    total_rain_to_day_tuple_ascending = sorted([(v, k) for (k, v) in day_to_rainfall_total_dict.items()], reverse=True)
    v, k = zip(*total_rain_to_day_tuple_ascending)
    print('The date with the most rain on average is the', k[0], '\nwith', (v[0] * .01), 'inches of rain.')


lines = import_web_data()
new_line_list = strip_split_slice_web_data(lines)
day_month_year_list, rainfall_int_list = get_rid_of_null_data_turn_numbers_to_int(new_line_list)
data_list_tuple = unzip_then_zip_data_for_tuple(day_month_year_list, rainfall_int_list)
rainfall_dict = create_dict_from_data_tuple(data_list_tuple)
print_single_day_with_most_rain(rainfall_dict)
year_to_rainfall_total_dict = create_year_to_rain_total_dict(rainfall_dict)
print_year_with_most_rain(year_to_rainfall_total_dict)
day_to_rainfall_total_dict = create_avg_day_to_rain_total_dict(rainfall_dict)
print_date_with_most_rain_on_average(day_to_rainfall_total_dict)



# USER INPUT - March 24th
