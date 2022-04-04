import requests
import csv
from main import standard_set_uris
from main import card_keys

afr_cards_1 = requests.get(standard_set_uris[0]['afr_1']).json()['data']
afr_cards_2 = requests.get(standard_set_uris[0]['afr_2']).json()['data']
afr_cards_3 = requests.get(standard_set_uris[0]['afr_3']).json()['data']

afr_pages = [afr_cards_1, afr_cards_2, afr_cards_3]

def alchemyCheck(card):
    return card['name'].startswith('A-')

with open('afr.csv', 'w', newline='\n', encoding='utf8') as csvfile:

    card_writer = csv.writer(csvfile, delimiter=',')

    for current_page in afr_pages:

        for card in current_page:

            # If necessary, we can call the enumerate() method on afr_cards to track the indices.
            # set_number = index + 1
        
            current_card = []

            if alchemyCheck(card):
                print('skipped card: ' + card['name'])
            else:
                for key in card_keys:

                    if key == 'image_uris':
                        current_card.append(card[key]['normal'])
                    elif key == 'prices':
                        new_prices = {'usd': '', 'usd_foil': ''}

                        for p_key in card[key]:
                            if p_key == 'usd':
                                new_prices['usd'] = card[key][p_key]
                            elif p_key == 'usd_foil':
                                new_prices['usd_foil'] = card[key][p_key]
                            else:
                                continue
                    
                        current_card.append(new_prices)
                    else:
                        if key in card:
                            current_card.append(card[key])

            if not alchemyCheck(card):
                card_writer.writerow(current_card)