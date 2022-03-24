import requests
import csv
from main import standard_set_uris
from main import card_keys

afr_cards = requests.get(standard_set_uris['afr']).json()['data']

with open('afr.csv', 'w', newline='\n') as csvfile:

    card_writer = csv.writer(csvfile, delimiter=',')

    for card in afr_cards:

        # If necessary, we can call the enumerate() method on afr_cards to track the indices.
        # set_number = index + 1
    
        current_card = []

        if card['name'].startswith("A-"):
            print('skipped card: ' + card['name'])
        else:
            for key in card_keys:

                if key == 'name':
                    if card[key].startswith("A-"):
                        break
                    else:
                        current_card.append(card[key])
                elif key == 'image_uris':
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
                    # else:
                    #     current_card.append('')

        # print(len(current_card))

        if len(current_card) > 0:
            card_writer.writerow(current_card)    