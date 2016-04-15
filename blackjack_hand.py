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

    def __eq__(self, other):
        pass

class Hand:
    """docstring for Hand"""
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        return 'Hand(cards: {})'.format(
            self.card_list
        )

    def add_card(self, new_card):
        self.card_list.append(instantiate_card_add_to_list(new_card))

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


class Deck:
    """docstring for Deck"""
    def __init__(self, list_of_cards):
        self.list_of_cards = list_of_cards

    def __repr__(self):
        return 'Deck(card: {})'.format(
            self.list_of_cards
        )

def prompt_user_for_cards():
    raw_cards = []

    more_cards = True
    while more_cards:
        user_cards = input('Enter a suit and card value separated by a single space:\n(type \'done\' to continue)\n> ')
        if user_cards != 'done':
            raw_cards.append(user_cards)
        else:
            more_cards = False
    return raw_cards

def instantiate_card_add_to_list(raw_list_of_cards):
    list_of_cards = []

    for item in raw_list_of_cards:
        list_of_cards.append(Card((item.split())[0], (item.split())[1]))
    return list_of_cards

def instantiate_hand(list_of_cards):
    return Hand(list_of_cards)

def get_new_card():
    return input('Enter a card suit and value separated by a single space:\n> ')


def main():
    # raw_list_of_cards = prompt_user_for_cards()
    raw_list_of_cards = ['diamonds ace', 'pizza 4']

    list_of_cards = instantiate_card_add_to_list(raw_list_of_cards)
    hand = instantiate_hand(list_of_cards)
    score = hand.score_hand()

    print(raw_list_of_cards)
    print(list_of_cards)

    hand.add_card(get_new_card())
    print(hand)
    print(score)

    if score > 21:
        print('Bust!')

main()
