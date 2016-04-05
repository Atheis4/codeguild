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

    def __str__(self):
        return 'Review: rating {}, text \'{}\''.format(
            self.rating, self.text
        )
    # def rating(self):


class Business:
    """Business"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Business name: {}'.format(
            self.name
        )

    def average_rating(self, rating):
        self.rating = statistics.mean(self.rating)



list_of_reviews = []

for dicts in raw_business_data:
    for review in dicts['reviews']:
        x = review['rating']
        y = review['text']
        list_of_reviews.append(Review(x, y))

print(Review)





# print(raw_business_data[0]['reviews'][0]['rating'])
# print(raw_business_data[0]['reviews'][0]['text'])
#
# print(first_review.rating, first_review.text)
# # first_review = BusinessReview()



#-------------------------------------------------------
# for item in raw_business_data[0]['reviews'][:]:
#     for key, value in item.items():
#         if key == 'rating':
#             salt_review.rating.append(value)
#         else:
#             salt_review.review_text.append(value)
#
#
# for item in raw_business_data[1]['reviews'][:]:
#     for key, value in item.items():
#         if key == 'rating':
#             voodoo_review.rating.append(value)
#         else:
#             voodoo_review.review_text.append(value)
#-------------------------------------------------------
