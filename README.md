# MTG-Script

This repository contains the code necessary to gather the data needed for a price-tracking and data visualization web app for Magic: The Gathering.

## Objectives

- Create Python script(s) which will:
  1. Make requests to an endpoint of the Scryfall API to get Card Data as JSON
  2. Convert Card Data JSON to a Python Dictionary
  3. Extract the desired data from the Dictionary
  4. Write the card data to a CSV file
- Load CSV into a database (likely MySQL)
- Use set data in service of front-end app

## TODO
- [x] Create a virtual environment for this project
- [x] Make HTTP requests using the requests library
- [x] Determine desired MTG sets
- [x] Explore small sample of card data from the set
- [x] Determine desired card data using keys found in JSON
- [x] Use the Python CSV module to write data to a CSV file
- [x] POC: full script that requests all cards from the set, extracts data from each card in the set, and then writes it to CSV
- [ ] Repackage conditionals used in writer file as "checkpoint functions," and then import those modules when necessary
- [ ] Build tests to maintain current code integrity and work towards TDD future
- [ ] MVP: a dynamic front-end application that allows the user to visualize card data loaded from an integrated back-end application

## Running This Code

You will need to create a new Python virtual environment. Load the dependencies located in `requirements.txt`.

This can be done from the terminal by activating your python virtual environment and then from the terminal running `pip3 install -r requirements.txt`.

Once your environment exists, is activated, and has the necessary 3rd party libraries you can run this example with `python afr_writer.py`.

The script will fire off many HTTP requests (using the requests library) to the scryfall API, parse the resulting JSON, extract the necessary information, and then write the data to a CSV file called `cards.csv`.
