import random

class Deck:
    """docstring for Deck"""
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Deck(cards: {})'.format(
            self.cards
        )

    # def __str__(self):
    #     return 'Cards in deck: {}'.format(
    #         self.cards
    #     )

class Card:
    """Docstring for Card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(
            self.value, self.suit
        )

    # def __repr__(self):
    #     return 'Card(suit: {}, value: {})'.format(
    #         self.suit, self.value
    #     )

class Hand:
    """Docstring for Hand"""
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return '{}'.format(
            self.cards
        )

    # def __repr__(self):
    #     return 'Hand(cards: {})'.format(
    #         self.cards
    #     )

def create_cards(suits, values_list):
    card_list_master = []
    # Nested list comprehension to build a complete list of cards
    [[card_list_master.append('{} {}'.format(suit, value)) for value in values_list] for suit in suits]
    return card_list_master

def create_deck(card_list_master):
    deck_list = []
    # List comprehension appends Card object with suit/value to deck_list
    [deck_list.append(Card(card.split()[0], card.split()[1])) for card in card_list_master]
    return deck_list

def deal_two_cards(deck_list):
    delt_cards_list = []
    for i in range(2):
        delt_cards_list.append(deck_list.pop(random.randint(0, len(deck_list) - 1)))
    return delt_cards_list

def draw_card_from_deck(deck_list):
    card = []
    card.append(deck_list.pop(random.randint(0, len(deck_list) - 1)))
    return card

def main():

    suits = 'spades hearts diamonds clubs'.split()
    values_list = ['ace', 'king', 'queen', 'jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    card_list_master = create_cards(suits, values_list)
    deck_list = create_deck(card_list_master)
    deck = Deck(deck_list)
    delt_cards_list = deal_two_cards(deck_list)

    player_hand = Hand(deal_two_cards(deck_list))
    dealer_hand = Hand(deal_two_cards(deck_list))

    # function for adding a card to a hand... Function might be better as a class method... Then the only thing that needs to happen is an updated list being passed into the method... Rather than the rigamorole I have currently...

    # Player one goes first... options - hit, Stay

    print('Your hand: {}.\nDealer hand: {}'.format(player_hand, dealer_hand))

    player_choice = input('Hit or stay?\n> ')


main()
