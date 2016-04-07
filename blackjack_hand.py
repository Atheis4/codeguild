import random

class Card:
    """docstring for Card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return 'Card(suit: {}, value: {})'.format(
            self.suit, self.value
        )

class Hand:
    """docstring for Hand"""
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        return 'Hand(cards: {})'.format(
            self.card_list
        )

    def hit(self):
        pass

    def score_hand(self):
        score = 0
        values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']

        for card in self.card_list:
            if card.value == 'ace':
                score += 1
            elif card.value in values[-3:]:
                score += 10
            else:
                score += int(card.value)
            if card.value == 'ace' and (score + 10) <= 21:
                score += 10
        return score

    def bust(self, score):
        pass

def prompt_user_for_cards():
    raw_list_of_cards = []

    more_cards = True
    while more_cards:
        user_cards = input('Enter a suit and card value separated by a single space:\n(type \'done\' to continue)\n> ')
        if user_cards != 'done':
            raw_list_of_cards.append(user_cards)
        else:
            more_cards = False
    return raw_list_of_cards

def instantiate_card_objects_in_list(raw_list_of_cards):
    split_suit_value_pair_list = []
    list_of_cards = []

    for item in raw_list_of_cards:
        split_suit_value_pair_list.append(item.split())
    for x, y in split_suit_value_pair_list:
        list_of_cards.append(Card(x, y))
    return list_of_cards

def instantiate_hand(list_of_cards):
    return Hand(list_of_cards)

def main():
    raw_list_of_cards = prompt_user_for_cards()
    list_of_cards = instantiate_card_objects_in_list(raw_list_of_cards)
    hand = instantiate_hand(list_of_cards)
    score = hand.score_hand()

    print(score)

    if score > 21:
        print('Bust!')

main()
