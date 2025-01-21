import csv
import sqlite3
from tkinter import messagebox

def generate_export_report():
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        # Fetch export data
        cursor.execute('SELECT * FROM exports1')  # Assuming exports1 table holds export data
        rows = cursor.fetchall()

        # Define the CSV file name
        file_name = "export_report.csv"

        # Create and write to CSV file
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Exporter ID", "Exporter Name", "Date", "Quantity", "Price per Unit", "Total Revenue"])  # Header
            writer.writerows(rows)  # Write all rows from the database

        conn.close()

        # Notify the user that the report has been generated
        messagebox.showinfo("Report Generated", f"Export report saved as {file_name}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Call the function to generate the report
generate_export_report()
