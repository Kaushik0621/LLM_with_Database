import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('dictionary.db')

# Query the data into a DataFrame
df = pd.read_sql_query('SELECT * FROM dictionary', conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
