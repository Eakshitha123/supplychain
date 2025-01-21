import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Query the imports1 table to get all entries
cursor.execute("SELECT * FROM imports1")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Print the rows (each row represents an entry in the imports1 table)
for row in rows:
    print(row)

# Close the database connection
conn.close()
