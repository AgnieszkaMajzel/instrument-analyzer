import sqlite3

conn = sqlite3.connect('price_modifiers.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS INSTRUMENT_PRICE_MODIFIER (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        value REAL NOT NULL
    )
''')

# Add a new price modifier
cursor.executemany('''
    INSERT INTO INSTRUMENT_PRICE_MODIFIER (name, value)
    VALUES (?, ?)
''', [
    ('INSTRUMENT1', 1.1),
    ('INSTRUMENT2', 0.9),
    ('INSTRUMENT3', 1.0),
    ('INSTRUMENT4', 1.15),
    ('INSTRUMENT5', 0.85),
])

# Commit the changes
conn.commit()
# Close the connection
conn.close()