import random

raw_business_data = [
  {
    'business_name': 'Salt & Straw',
  },
  {
    'business_name': 'Voodoo Donuts',
  },
]
raw_user_data = [
  {'user_name': 'Abby'},
  {'user_name': 'Helen'},
  {'user_name': 'Bobby'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]

class Review:
    """Business Review"""
    def __init__(self, user_name, business_name, rating, text):
        self.user_name = user_name
        self.business_name = business_name
        self.rating = rating
        self.text = text

    def __repr__(self):
        return 'Review(user: {}, business: {}, rating: {}, text: \'{}\')'.format(
            self.user_name, self.business_name, self.rating, self.text
        )

class Business:
    """Business"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Business(name: {})'.format(
            self.name
        )

class User:
    """User"""
    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return 'User(name: {})'.format(
            self.user_name
        )


def instantiate_reviews_save_to_list(data):
    reviews_list = []

    for review_dict in data:
        a = review_dict['user_name']
        b = review_dict['business_name']
        c = review_dict['rating']
        d = review_dict['text']
        reviews_list.append(Review(a, b, c, d))

    return reviews_list


def create_total_user_set(reviews_list):
    sum_user_list = []
    sum_user_list = [review.user_name for review in reviews_list]
    sum_user_set = set(sum_user_list)
    return sum_user_set


def filter_reviews_to_name(reviews_list, user_name):
    unique_user_reviews_list = []

    for review_object in reviews_list:
        if user_name in review_object.user_name:
            unique_user_reviews_list.append(review_object)

    return unique_user_reviews_list


def main():
    reviews_list = instantiate_reviews_save_to_list(raw_review_data)
    sum_user_set = create_total_user_set(reviews_list)


    lookup = True

    while lookup:
        user_search = input('Which user\'s reviews would you like to find?\n(type \'done\' to quit)\n> ')
        if user_search == 'done':
            lookup = False

        if user_search in sum_user_set:
            unique_user_reviews_list = filter_reviews_to_name(reviews_list, user_search)

            print(unique_user_reviews_list)

        else:
            print('We don\'t have reviews from that user.\n')

main()
