standard_set_uris = [
    # 'znr': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints',
    # 'khm': 'https://api.scryfall.com/cards/search?order=set&q=e%3Akhm&unique=prints',
    # 'stx': 'https://api.scryfall.com/cards/search?order=set&q=e%3Astx&unique=prints',

    # TODO build this into a class
    {
        'afr_1': 'https://api.scryfall.com/cards/search?order=set&q=e%3Aafr&unique=prints',
        'afr_2': 'https://api.scryfall.com/cards/search?format=json&include_extras=false&include_multilingual=false&order=set&page=2&q=e:afr&unique=prints',
        'afr_3': 'https://api.scryfall.com/cards/search?format=json&include_extras=false&include_multilingual=false&order=set&page=3&q=e:afr&unique=prints'
    }
    # 'mid': 'https://api.scryfall.com/cards/search?order=set&q=e%3Amid&unique=prints',
    # 'vow': 'https://api.scryfall.com/cards/search?order=set&q=e%3Avow&unique=prints',
    # 'neo': 'https://api.scryfall.com/cards/search?order=set&q=e%3Avow&unique=prints'
]

# TODO: make list of keys for each standard set

card_keys = ['name', 'uri', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'colors', 'color_identity', 'foil', 'nonfoil' 'set', 'set_name', 'rarity', 'artist', 'prices']