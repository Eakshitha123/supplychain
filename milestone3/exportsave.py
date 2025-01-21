import sqlite3
from tkinter import messagebox

def check_export_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Query the exports1 table to get all entries
    cursor.execute("SELECT * FROM exports1")

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # If there are no rows, show a message that no data is saved
    if not rows:
        messagebox.showinfo("Check Export Data", "No export data found in the database.")
    else:
        # Print the rows (each row represents an entry in the exports1 table)
        for row in rows:
            print(row)  # You can also use messagebox.showinfo to display the data in a popup if you prefer

        messagebox.showinfo("Check Export Data", "Export data is saved in the database!")

    # Close the database connection
    conn.close()

# Call this function to check the export data after saving
check_export_data()
