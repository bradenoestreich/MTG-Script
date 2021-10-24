import requests

standard_set_uris = {
    'znr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints',
    'khm': 'https://api.scryfall.com/cards/search?order=set&q=e%3Akhm&unique=prints',
    'stx': 'https://api.scryfall.com/cards/search?order=set&q=e%3Astx&unique=prints',
    'afr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aafr&unique=prints',
    'mid': 'https://api.scryfall.com/cards/search?order=set&q=e%3Amid&unique=prints',
}

set_uri = standard_set_uris['khm']

set_json = requests.get(set_uri).json()
cards = set_json['data']

set_json_two = requests.get(set_json['next_page']).json()
cards_two = set_json_two['data']

set_json_three = requests.get(set_json_two['next_page']).json()
cards_three = set_json_three['data']

index = -1

for card in cards:
    
    index += 1
    set_number = index + 1

    # print('Index: ' + str(index))
    print(str(set_number) + ' ' + card['name'])

    if 'card_faces' in card:
        card_front = card['card_faces'][0]['image_uris']['normal']
        card_back = card['card_faces'][1]['image_uris']['normal']
        print(card_front)
        print(card_back)
    else:
        print(card['image_uris']['normal'])

    print('\n')

    # TODO: cards that have multiple faces have their 'image_uris' nested within a 'card_faces' key, so the logic will have to accomodate that.
    # COMPLETE
