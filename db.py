import sqlite3

class PriceModifierDB:
    def __init__(self, db_name'price_modifiers.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

# Create the table if it doesn't exist
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS INSTRUMENT_PRICE_MODIFIER (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                value REAL NOT NULL
            )
        ''')
        self.conn.commit()

# Add a new price modifier
    def add_modifier(self, name, modifier):
        self.cursor.execute('''
            INSERT INTO INSTRUMENT_PRICE_MODIFIER (name, modifier)
            VALUES (?, ?)
        ''', (name, modifier))
        self.conn.commit()

# Get a price modifier
    def get_modifiers(self, instrument_name):
        self.cursor.execute('SELECT MODIFIER FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = ?', (instrument_name,))
        row = self.cursor.fetchone()
        return row[0] if row else 1.0 # Default modifier is 1.0
    
    def close(self):
        self.conn.close()