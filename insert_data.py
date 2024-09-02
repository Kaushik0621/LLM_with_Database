import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/dictionary.db')

# Create a cursor object
cursor = conn.cursor()

# Insert data into the dictionary table
words = [
    ('apple', 'A fruit that is typically round and red, green, or yellow, with crisp flesh and a sweet taste.'),
    ('banana', 'A long, curved fruit with a yellow skin and soft, sweet, white flesh inside.'),
    ('cat', 'A small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws.'),
    ('dog', 'A domesticated carnivorous mammal that typically has a long snout and an acute sense of smell.'),
]

cursor.executemany('INSERT OR IGNORE INTO dictionary (word, meaning) VALUES (?, ?)', words)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully, duplicates were skipped.")
