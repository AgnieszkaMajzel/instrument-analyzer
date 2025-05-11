import sqlite3
import time

class PriceModifierDB:
    def __init__(self, db_name='price_modifiers.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cache = {}

# Get a price modifier
    def get_modifiers(self, name):
        now = time.time()
        if name in self.cache:
            value, last_update = self.cache[name]
            if now - last_update < 5:
                return value
            
        self.cursor.execute('SELECT VALUE FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = ?', (name,))
        row = self.cursor.fetchone()
        if row:
            value = row[0]
            self.cache[name] = (value, now)
            return value
        else:
            self.cache[name] = (1.0, now) # Default modifier is 1.0
            return 1.0
    
    def close(self):
        self.conn.close()