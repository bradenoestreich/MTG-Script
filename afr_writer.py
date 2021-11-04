import requests
import csv
from main import standard_set_uris
from main import our_keys

afr_cards = requests.get(standard_set_uris['afr']).json()['data']

with open('afr.csv', 'w', newline='\n') as csvfile:

    card_writer = csv.writer(csvfile, delimiter=',')

    for index, card in enumerate(afr_cards):

        set_number = index + 1
    
        current_card = []

        for key in our_keys:

            if key == 'image_uris':
                current_card.append(card[key]['normal'])
            else:
                if key in card:
                    current_card.append(card[key])
                else:
                    current_card.append('')

        print(len(current_card))

        card_writer.writerow(current_card)