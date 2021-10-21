import requests

standard_set_uris = {
    'znr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints',
    'khm': 'https://api.scryfall.com/cards/search?order=set&q=e%3Akhm&unique=prints',
    'stx': 'https://api.scryfall.com/cards/search?order=set&q=e%3Astx&unique=prints',
    'afr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aafr&unique=prints',
    'mid': 'https://api.scryfall.com/cards/search?order=set&q=e%3Amid&unique=prints',
}

set_uri = standard_set_uris['znr']

# set_request = requests.get(set_uri)

# set_json = set_request.json()

set_json = requests.get(set_uri).json()

first_card = set_json['data'][0]

print(first_card['name'])
print(first_card['image_uris']['large'])
