import csv
from collections import defaultdict
from instrument import InstrumentData #Import the InstrumentData class

#create a dictionary to hold the instrument data
instrument = defaultdict(InstrumentData)

# Read the CSV file
with open('data.txt', 'r') as file:
    reader = csv.reader(file)

    # Initialize InstrumentData explicitly when processing each row
    for row in reader:
        name, date_str, value_str = row
        if name not in instrument:
            instrument[name] = InstrumentData(name)
        instrument[name].add_record(date_str, value_str)
        
# Print the results
for name, instrument in instrument.items():
    results = instrument.get_results()
    print(f"{name}: {instrument.get_results()}")

# The code reads a CSV file named 'data.txt' and processes the data for different instruments.
