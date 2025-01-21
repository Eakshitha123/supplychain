import sqlite3

def create_db():
    # Connect to SQLite database (this will create the database file if it doesn't exist)
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Create the 'imports1' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imports1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_id TEXT,
            supplier_name TEXT,
            date TEXT,
            quantity INTEGER,
            price_per_unit REAL,
            total_cost REAL
        )
    ''')

    # Create the 'exports1' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exports1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exporter_id TEXT,
            exporter_name TEXT,
            date TEXT,
            quantity INTEGER,
            price_per_unit REAL,
            total_revenue REAL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Database and tables created successfully.")
