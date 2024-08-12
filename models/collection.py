from cards import Card
from deck import Deck


class Collection:
    def __init__(self):
        self.decks = []
        self.cards = []

    def add_deck(self, deck_name):
        new_deck = Deck(name=deck_name)
        self.decks.append(new_deck)

    def remove_deck(self):
        pass

    def add_card(self, name, set_name, set_code, rarity, col_num, card_type):
        new_card = Card(name=name, set_name=set_name, set_code=set_code, rarity=rarity, collection_number=col_num,
                        card_type=card_type, image_url=None)
        self.cards.append(new_card)

    def remove_card(self):
        pass

    def search_card(self):
        # TODO: Search with multiple optional parameters
        pass

