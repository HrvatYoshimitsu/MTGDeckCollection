import requests


class Card:
    SCRYFALL_API_URL = "https://api.scryfall.com/cards/search"

    def __init__(self, name, set_name, set_code, rarity, collection_number, card_type, image_url):
        self.name = name
        self.set_name = set_name
        self.set_code = set_code
        self.rarity = rarity
        self.collection_number = collection_number
        self.card_type = card_type
        self.image_url = image_url

    def __str__(self):
        return (f"Card Name: {self.name}\n"
                f"Set Name: {self.set_name}\n"
                f"Card Type: {self.card_type}")

    @staticmethod
    def search_card_scryfall(name, set_code, collection_number):
        response = requests.get(f"{Card.SCRYFALL_API_URL}?&q=!{name.replace(" ", "")}+set%3a{set_code}+cn%3A{collection_number}")
        if response.status_code == 200:
            return response.json()
        else:
            print("Error")


if __name__ == "__main__":
    test_card = Card(name="testing", set_name="Test Set", set_code="TST", rarity="Mythic", collection_number=000, card_type="Test", image_url=None)
    print(test_card)

    Card.search_card_scryfall("sol ring", "pip", "359")