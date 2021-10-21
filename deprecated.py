import requests

# Requesting a single card based on the search term 'alrund'

card_request = requests.get('https://api.scryfall.com/cards/search?q=alrund')
card_json = card_request.json()
print(card_json['data'][1]['image_uris']['large'])

# Requesting the Kaldheim set programmatically from Alrund's Epiphany

card_data = card_json['data']

khm_set_uri = card_data[1]['set_search_uri']

khm_set_request = requests.get(khm_set_uri)

khm_json = khm_set_request.json()