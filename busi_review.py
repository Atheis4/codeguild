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

    def average_rating(self, rating):
        pass



list_of_reviews = []

for dicts in raw_business_data:
    # print(dicts)
    Business(dicts['business_name'], dicts['reviews'])
    for review in dicts['reviews']:
        x = review['rating']
        y = review['text']
        list_of_reviews.append(Review(x, y))




# for i in list_of_reviews:
#     print(i.rating, i.text)
#
# for raw_business_data['business_name']:
#     print(raw_business_data['business_name'])

# voodoo = Business('Voodoo', [])
#
# new_list = [Review(3, 'great!')]
#
#
# voodoo = Business('Voodoo', new_list)
#
# print(voodoo)




#
# for x, y in word_pair_list:
#     if x not in paired_word_dict:
#         paired_word_dict[x] = {}
#     if y not in paired_word_dict[x]:
#         paired_word_dict[x][y] = 0
#     paired_word_dict[x][y] += 1




# new_dict = {k=business_name: {k2=rating: v=?, k3=text: v=?}}
