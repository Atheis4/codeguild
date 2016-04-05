import statistics
import math

raw_business_data = [
  {
    'business_name': 'Salt & Straw',
    'reviews': [
      {'rating': 5, 'text': 'Lucious ice cream!'},
      {'rating': 4, 'text': 'Super tasty, but such a long line!'},
      {'rating': 2, 'text': 'Overrated, but I like sugar.'}
    ],
  },
  {
    'business_name': 'Voodoo Donuts',
    'reviews': [
      {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
      {'rating': 5, 'text': 'Pink building is so cute!'},
      {'rating': 2, 'text': 'Diabetes inducing.'}
    ],
  },
]


class Review:
    """Business Review"""
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text

    def __repr__(self):
        return 'Review(rating: {}, text: \'{}\')'.format(
            self.rating, self.text
        )


class Business:
    """Business"""
    def __init__(self, name, reviews):
        self.name = name
        self.reviews = reviews

    def __repr__(self):
        return 'Business(name: {}, reviews: {})'.format(
            self.name, self.reviews
        )

    def find_average(self):
        listy = []
        for review in self.reviews:
            listy.append(review.rating)
        print(statistics.mean(listy))




def instantiate_review_and_biz_classes_append_to_list(raw_business_data):
    list_of_businesses = []

    for dicts in raw_business_data:
        reviews_list = []
        for review in dicts['reviews']:
            x = review['rating']
            y = review['text']
            reviews_list.append(Review(x, y))
        list_of_businesses.append(Business(dicts['business_name'], reviews_list))
    return list_of_businesses


list_of_businesses = instantiate_review_and_biz_classes_append_to_list(raw_business_data)


for i in list_of_businesses:
    rating_list = []
    for x in i.reviews:
        rating_list.append(x.rating)
    # print(statistics.mean(rating_list))


# for j in list_of_businesses:
    # print(j.find_average)

first_biz = list_of_businesses[0]

avg_rating = Business.find_average(first_biz)
