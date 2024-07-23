class Card:
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