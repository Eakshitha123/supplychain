import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class ExportsModule:
    def __init__(self, root):
        self.root = root
        self.root.title("Exports Module")
        self.root.geometry("400x500")

        # Title Label
        self.title_label = tk.Label(self.root, text="Enter Export Details", font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=10)

        # Exporter ID
        self.exporter_id_label = tk.Label(self.root, text="Exporter ID:")
        self.exporter_id_label.pack(pady=5)
        self.exporter_id_entry = tk.Entry(self.root)
        self.exporter_id_entry.pack(pady=5)

        # Exporter Name
        self.exporter_name_label = tk.Label(self.root, text="Exporter Name:")
        self.exporter_name_label.pack(pady=5)
        self.exporter_name_entry = tk.Entry(self.root)
        self.exporter_name_entry.pack(pady=5)

        # Date
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.pack(pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)

        # Quantity
        self.quantity_label = tk.Label(self.root, text="Quantity:")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)

        # Price per Unit
        self.price_label = tk.Label(self.root, text="Price per Unit:")
        self.price_label.pack(pady=5)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack(pady=5)

        # Total Revenue (calculated)
        self.total_revenue_label = tk.Label(self.root, text="Total Revenue:")
        self.total_revenue_label.pack(pady=5)
        self.total_revenue_value = tk.Label(self.root, text="0.0")
        self.total_revenue_value.pack(pady=5)

        # Button to calculate total revenue
        self.calculate_button = tk.Button(self.root, text="Calculate Total Revenue", command=self.calculate_total_revenue)
        self.calculate_button.pack(pady=10)

        # Button to save data
        self.save_button = tk.Button(self.root, text="Save Export", command=self.save_export)
        self.save_button.pack(pady=10)

    def calculate_total_revenue(self):
        try:
            # Get the values from the entry fields
            quantity = int(self.quantity_entry.get())
            price_per_unit = float(self.price_entry.get())
            total_revenue = quantity * price_per_unit
            self.total_revenue_value.config(text=str(total_revenue))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for Quantity and Price per Unit.")

    def save_export(self):
        # Get values from entry fields
        exporter_id = self.exporter_id_entry.get()
        exporter_name = self.exporter_name_entry.get()
        date = self.date_entry.get()
        quantity = self.quantity_entry.get()
        price_per_unit = self.price_entry.get()

        # Validate inputs
        if not exporter_id or not exporter_name or not date or not quantity or not price_per_unit:
            messagebox.showerror("Missing Data", "Please fill in all fields.")
            return

        try:
            quantity = int(quantity)
            price_per_unit = float(price_per_unit)
            total_revenue = quantity * price_per_unit
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity and Price per Unit must be numbers.")
            return

        # Check if the quantity to export is available in inventory
        if not self.check_inventory(quantity):
            messagebox.showerror("Insufficient Inventory", "Not enough inventory to export this quantity.")
            return

        # Save to database
        try:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO exports1 (exporter_id, exporter_name, date, quantity, price_per_unit, total_revenue)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (exporter_id, exporter_name, date, quantity, price_per_unit, total_revenue))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Export saved successfully!")
            self.clear_fields()  # Clear the form after saving

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def check_inventory(self, export_quantity):
        # Check if there is enough inventory for export
        try:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()

            cursor.execute('SELECT SUM(quantity) FROM imports1')
            total_inventory = cursor.fetchone()[0] or 0

            conn.close()

            if total_inventory >= export_quantity:
                return True
            else:
                return False
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while checking inventory: {e}")
            return False

    def clear_fields(self):
        # Clear all input fields
        self.exporter_id_entry.delete(0, tk.END)
        self.exporter_name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.total_revenue_value.config(text="0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExportsModule(root)
    root.mainloop()
