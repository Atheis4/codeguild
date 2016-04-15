class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return 'Card(suit: {}, value: {})'.format(
            self.suit, self.value
        )

class Hand:
    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        return 'Hand(cards: {})'.format(
            self.card_list
        )

    def add_to(self, new_card):
        list_of_cards.append(instantiate_card(new_card))
        return list_of_cards

    def score(self):
        score = 0
        values = ['ace', 'jack', 'queen', 'king']
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

def get_user_cards():
    raw_card_list = []
    more_cards = True

    while more_cards:
        new_card = input('Enter a suit and value separated by a single space:\n(type \'done\' to quit)\n> ')
        if new_card != 'done':
            raw_card_list.append(new_card)
        else:
            more_cards = False
    return raw_card_list

def instantiate_card(raw_card):
    return Card(raw_card.split()[0], raw_card.split()[1])

def build_hand(raw_card_list):
    for card in raw_card_list:
        list_of_cards.append(instantiate_card(card))
    return Hand(list_of_cards)

list_of_cards = []
new_hand = Hand(list_of_cards)
hand = build_hand(get_user_cards())
# hand.add_to()
score = hand.score()

print(hand)
print(list_of_cards)
print(score)


# Add another Hand for Dealer
# Create Deck
# Create randomness in drawing cards
# Hit, Stay, split
