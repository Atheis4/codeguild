import random

class Deck:
    """docstring for Deck"""
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Deck(cards: {})'.format(self.cards)

    def deal_two(self):
        delt_cards = []
        for i in range(2):
            delt_cards.append(self.cards.pop(random.randint(0, len(self.cards) - 1)))
        return delt_cards

    def hit(self):
        new_card = []
        new_card.append(self.cards.pop(random.randint(0, len(self.cards) - 1)))
        return new_card

class Card:
    """Docstring for Card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)

class Hand:
    """Docstring for Hand"""
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return 'Hand(cards: {})'.format(self.cards)

    def score(self):
        score = 0
        values = 'ace king queen jack'.split()

        for card in self.cards:
            if card.value == 'ace':
                score += 1
            elif card.value in values[1:]:
                score += 10
            else:
                score += int(card.value)
        for card in self.cards:
            if card.value == 'ace' and (score + 10) <= 21:
                score += 10
        return score

def create_cards():
    suits = 'spades hearts diamonds clubs'.split()
    values_list = ['ace', 'king', 'queen', 'jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    card_list_master = []
    # Nested list comprehension to build a complete list of 52 cards
    [[card_list_master.append('{} {}'.format(suit, value)) for value in values_list] for suit in suits]
    return card_list_master

def create_deck(card_list):
    deck_list = []
    # List comprehension appends Card object with suit/value to deck_list
    [deck_list.append(Card(card.split()[0], card.split()[1])) for card in card_list]
    return deck_list

def main():
    deck = Deck(create_deck(create_cards()))

    player_hand = Hand(deck.deal_two())
    dealer_hand = Hand(deck.deal_two())

    print('\nYour hand: {}, score: {}\nDealer hand: {}, score {}\n'.format(player_hand, player_hand.score(), dealer_hand, dealer_hand.score()))

    player_hand.cards += deck.hit()
    print(player_hand, player_hand.score())
    

if __name__ == "__main__":
    main()
