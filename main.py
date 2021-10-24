import requests

standard_set_uris = {
    'znr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints',
    'khm': 'https://api.scryfall.com/cards/search?order=set&q=e%3Akhm&unique=prints',
    'stx': 'https://api.scryfall.com/cards/search?order=set&q=e%3Astx&unique=prints',
    'afr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aafr&unique=prints',
    'mid': 'https://api.scryfall.com/cards/search?order=set&q=e%3Amid&unique=prints',
}

set_uri = standard_set_uris['afr']

set_json = requests.get(set_uri).json()
cards = set_json['data']

set_json_two = requests.get(set_json['next_page']).json()
cards_two = set_json_two['data']

set_json_three = requests.get(set_json_two['next_page']).json()
cards_three = set_json_three['data']

tally = -1

for card in cards:
    
    tally += 1

    print(str(tally) + ' ' + card['name'])
    print(card['image_uris']['large'])
    print('\n')

    # Unexpected problem: cards that have multiple faces have their 'image_uris' nested within a 'card_faces' key, so the logic will have to accomodate that.
