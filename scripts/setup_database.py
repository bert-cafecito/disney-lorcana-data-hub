import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/processed/disney_lorcana.db')

# Create a cursor object
cur = conn.cursor()

# Create cards table query
create_cards_table = '''
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
'''

# Execute the create cards table query
cur.execute(create_cards_table)

# Commit the changes
conn.commit()

# Close the connection
conn.close()