class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, new_card):
        for card in self.cards:
            if new_card.name == card.name:
                print("Card already exists in the deck")
                return
        self.cards.append(new_card)

    def remove_card(self, card_name):
        for card in self.cards:
            if card_name == card.name:
                self.cards.remove(card)
                print("removed card")
                return

