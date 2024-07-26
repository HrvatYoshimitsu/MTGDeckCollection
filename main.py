from models import cards

is_running = True

while is_running:
    selection = input(f"(S)earch Card\n(E)xit\n").lower()
    if selection == 'e':
        is_running = False
    elif selection == 's':
        card_name = input("Name of the card: ")
        set_code = input("3 letter set code: ")
        collection_number = input("Collection number: ")
        print(cards.Card.search_card_scryfall(card_name, set_code, collection_number))
