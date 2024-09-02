import sqlite3
import os

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/dictionary.db')

# Create a cursor object
cursor = conn.cursor()

# Create the dictionary table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dictionary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE,
    meaning TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
