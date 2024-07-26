from models.cards import Card
import unittest


class TestCards(unittest.TestCase):
    def setUp(self):
        self.test_card = Card(name="test_card", set_name="Test Set", set_code="tst", rarity="Mythic",
                              collection_number=000, card_type="test", image_url=None)

    def test_scryfall_search(self):
        print("Running test_scryfall_search")
        test_card = Card.search_card_scryfall(name="sol ring", set_code="pip", collection_number="359")
        self.assertIsNotNone(test_card)


