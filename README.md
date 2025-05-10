# Instrument Analyzer

## Overview
The Instrument Analyzer is a Python-based program designed to process and analyze financial instrument data from a CSV file. It calculates various metrics for different instruments, such as averages, minimum values, and sums of the newest values. Additionally, it applies price modifiers stored in a SQLite database to adjust the raw data.

## Features
- **Data Processing**: Reads instrument data from a CSV file (`data.txt`).
- **Price Modifiers**: Adjusts raw values using modifiers stored in a SQLite database (`price_modifiers.db`).
- **Custom Metrics**:
  - Mean for `INSTRUMENT1`.
  - Mean for `INSTRUMENT2` (data from November 2014).
  - Minimum value for `INSTRUMENT3`.
  - Sum of the newest 10 values for other instruments.
- **Database Management**: Includes scripts to initialize and populate the database with default modifiers.

## File Structure
- `reader.py`: Main script to read and process the data.
- `instrument.py`: Contains the `InstrumentData` class for managing instrument-specific data and calculations.
- `db.py`: Manages the SQLite database for price modifiers.
- `init_db.py`: Initializes the database and populates it with default modifiers.
- `data.txt`: Input CSV file containing instrument data.
- `price_modifiers.db`: SQLite database file for storing price modifiers.
- `run.bat`: Batch script to run the program on Windows.

## How to Run
1. Ensure Python 3.11 or later is installed on your system.
2. Install SQLite if not already available.
3. Run the batch script:
   ```
   run.bat
   ```
   This will initialize the database and execute the main program.

## Example Input (`data.txt`)
```
INSTRUMENT1,01-Jan-1996,2.4655
INSTRUMENT1,02-Jan-1996,2.4685
INSTRUMENT5,18-Apr-2003,3.91
```

## Example Output
```
INSTRUMENT1: 2.5
INSTRUMENT5: 3.32
```

## Dependencies
- Python 3.11 or later
- SQLite

## License
This project is licensed under the MIT License.