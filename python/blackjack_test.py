import unittest
import blackjack

class Blackjack(unittest.TestCase):
    def test_deck_init(self):
        cards_list = ['ace', 'spades']
        deck = blackjack.Deck(cards_list)
        assert deck.cards == ['ace', 'spades']

