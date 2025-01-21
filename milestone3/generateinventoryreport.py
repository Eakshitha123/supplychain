import csv
import sqlite3
from tkinter import messagebox

def generate_inventory_report():
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        # Fetch inventory data
        cursor.execute('SELECT * FROM imports1')  # Assuming imports1 table holds inventory data
        rows = cursor.fetchall()

        # Define the CSV file name
        file_name = "inventory_report.csv"

        # Create and write to CSV file
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Supplier ID", "Supplier Name", "Date", "Quantity", "Price per Unit", "Total Cost"])  # Header
            writer.writerows(rows)  # Write all rows from the database

        conn.close()

        # Notify the user that the report has been generated
        messagebox.showinfo("Report Generated", f"Inventory report saved as {file_name}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Call the function to generate the report
generate_inventory_report()
