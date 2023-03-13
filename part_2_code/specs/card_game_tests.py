import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Five", 5)
        self.card2 = Card("Ace", 1)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        results = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, results)

    def test_highest_card(self):
        results = self.card_game.highest_card(self.card2, self.card1)
        self.assertEqual(self.card1, results)

    def test_cards_total(self):
        results = self.card_game.cards_total([self.card1, self.card2])
        self.assertEqual("You have a total of 6", results)
    