import csv
from collections import defaultdict
from instruments import InstrumentData # Import the InstrumentData class

#create a dictionary to hold the instrument data
instruments = defaultdict(InstrumentData)

# Read the CSV file
with open('data.txt', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        name, date_str, value_str = row
        instruments[name].add_record(date_str, value_str)
        
# Print the results
for name, instrument in instruments.items():
    results = instrument.get_results()
    print(f"{name}: {instrument.get_results()}")

# The code reads a CSV file named 'data.txt' and processes the data for different instruments.
