import csv
from collections import defaultdict
from instrument import InstrumentData #Import the InstrumentData class
from db import PriceModifierDB #Import the PriceModifierDB class

instruments = {} # Create a dictionary to hold the instrument data
db = PriceModifierDB('price_modifiers.db')

# Read the CSV file
with open('data.txt', 'r') as file:
    reader = csv.reader(file)
    
    # The modifier calculation
    for row in reader:
        name, date_str, value_str = row
        try:
            raw_value = float(value_str)
        except ValueError:
            continue

        modifier = db.get_modifiers(name)
        value = raw_value * modifier

        if name not in instruments:
            instruments[name] = InstrumentData(name)
        instruments[name].add_record(date_str, value)
    
# Print the results
for name, instruments in instruments.items():
    results = instruments.get_results()
    print(f"{name}: {instruments.get_results()}")

# The code reads a CSV file named 'data.txt' and processes the data for different instruments.
