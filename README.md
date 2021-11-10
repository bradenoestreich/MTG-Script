# MTG-Application Data Work

This repository contains the code necessary to gather the data needed for a web app.

## Objectives

Python script(s) which will:
  1. Make requests to the Scryfall API to get Card Data as JSON
  2. Convert Card Data JSON to a Python Dictionary
  3. Extract the data we care about from the Dictionary
  4. Write the card data to a CSV file

After we have a CSV file with all of the card data we care about we can create another script that will load all of the records into a Database that can be used by the resulting web application.

## Todo

- [x] Create a virtual environment for this project
- [x] Make HTTP requests using the requests library
- [x] Determine MTG sets we care about
- [x] Explore small sample of card data from each set
- [x] Determine card data we care about
- [x] Use the Python csv module to write data to a CSV file
- [x] POC: extract data from small sample of cards and write them to CSV file
- [ ] MVP: full script that requests all cards from all sets, extracts data from each card in each set, and then writes it to CSV

## Running This Code

You will need to create a new Python virtual environment. Load the dependencies located in `requirements.txt`.

This can be done from the terminal by activating your python virtual environment and then from the terminal running `pip3 install -r requirements.txt`.

Once your environment exists, is activated, and has the necessary 3rd party libraires you can run this example with `python3 main.py`.

The script will fire off many HTTP requests (using the requests library) to the scryfall API, parse the resulting JSON, extract the necessary information, and then write the data to a CSV file called `cards.csv`.
