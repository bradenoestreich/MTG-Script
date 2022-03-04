import requests
import csv

standard_set_uris = {
    # 'znr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints',
    # 'khm': 'https://api.scryfall.com/cards/search?order=set&q=e%3Akhm&unique=prints',
    # 'stx': 'https://api.scryfall.com/cards/search?order=set&q=e%3Astx&unique=prints',
    'afr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aafr&unique=prints',
    # 'mid': 'https://api.scryfall.com/cards/search?order=set&q=e%3Amid&unique=prints',
    # 'vow': 'https://api.scryfall.com/cards/search?order=set&q=e%3Avow&unique=prints',
    # 'neo': 'https://api.scryfall.com/cards/search?order=set&q=e%3Avow&unique=prints'
}

# set_uri = standard_set_uris['afr']

# set_json = requests.get(set_uri).json()
# cards = set_json['data']

# set_json_two = requests.get(set_json['next_page']).json()
# cards_two = set_json_two['data']

# set_json_three = requests.get(set_json_two['next_page']).json()
# cards_three = set_json_three['data']

# TODO: make list of keys for each standard set

# our_keys = ['name', 'uri', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'colors', 'color_identity', 'keywords', 'set', 'set_name', 'rarity', 'flavor_text', 'artist']

new_keys = ['name', 'uri', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'colors', 'color_identity', 'foil', 'nonfoil' 'set', 'set_name', 'rarity', 'artist', 'prices']

# new_keys = ['name', 'uri']

# with open('cards.csv', 'w', newline='\n') as csvfile:

#     card_writer = csv.writer(csvfile, delimiter=',')

#     for index, card in enumerate(cards):
        
#         set_number = index + 1

#         card_name = card['name']
#         print(set_number, card_name)
#         card_front = ''
#         card_back = ''

#         if 'card_faces' in card:
#             card_front = card['card_faces'][0]['image_uris']['normal']
#             card_back = card['card_faces'][1]['image_uris']['normal']
#             print(card_front)
#             print(card_back)
#         else:
#             card_front = card['image_uris']['normal']
#             print(card_front)

#         print('\n')
#         card_writer.writerow([card_name, card_front, card_back])

#         # TODO: cards that have multiple faces have their 'image_uris' nested within a 'card_faces' key, so the logic will have to accomodate that.
#         # COMPLETE