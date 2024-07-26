from models.cards import Card
from models.deck import Deck
import unittest


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck("Test Deck")
        self.test_card = Card(name="test_card", set_name="Test Set", set_code="tst", rarity="Mythic",
                              collection_number=000, card_type="test", image_url=None)

    def test_add_card(self):
        print("Running test_add_card")
        self.deck.add_card(self.test_card)
        self.assertEqual(len(self.deck.cards), 1)
        self.deck.add_card(self.test_card)
        self.assertEqual(len(self.deck.cards), 1)

    def test_remove_card(self):
        print("Running test_remove_card")
        self.deck.add_card(self.test_card)
        self.deck.remove_card(self.test_card.name)
        self.assertEqual(len(self.deck.cards), 0)