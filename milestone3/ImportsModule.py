import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class ImportsModule:
    def __init__(self, root):
        self.root = root
        self.root.title("Imports Module")
        self.root.geometry("400x450")
        self.root.config(bg="#f2f2f2")  # Light grey background for the window
        
        # Title Label with custom font and color
        self.title_label = tk.Label(self.root, text="Enter Import Details", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
        self.title_label.pack(pady=10, fill="both")

        # Supplier ID
        self.supplier_id_label = tk.Label(self.root, text="Supplier ID:", font=("Arial", 12), bg="#f2f2f2")
        self.supplier_id_label.pack(pady=5, anchor="w", padx=20)
        self.supplier_id_entry = tk.Entry(self.root, font=("Arial", 12))
        self.supplier_id_entry.pack(pady=5, padx=20, fill="x")

        # Supplier Name
        self.supplier_name_label = tk.Label(self.root, text="Supplier Name:", font=("Arial", 12), bg="#f2f2f2")
        self.supplier_name_label.pack(pady=5, anchor="w", padx=20)
        self.supplier_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.supplier_name_entry.pack(pady=5, padx=20, fill="x")

        # Date
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="#f2f2f2")
        self.date_label.pack(pady=5, anchor="w", padx=20)
        self.date_entry = tk.Entry(self.root, font=("Arial", 12))
        self.date_entry.pack(pady=5, padx=20, fill="x")

        # Quantity
        self.quantity_label = tk.Label(self.root, text="Quantity:", font=("Arial", 12), bg="#f2f2f2")
        self.quantity_label.pack(pady=5, anchor="w", padx=20)
        self.quantity_entry = tk.Entry(self.root, font=("Arial", 12))
        self.quantity_entry.pack(pady=5, padx=20, fill="x")

        # Price per Unit
        self.price_label = tk.Label(self.root, text="Price per Unit:", font=("Arial", 12), bg="#f2f2f2")
        self.price_label.pack(pady=5, anchor="w", padx=20)
        self.price_entry = tk.Entry(self.root, font=("Arial", 12))
        self.price_entry.pack(pady=5, padx=20, fill="x")

        # Total Cost (calculated)
        self.total_cost_label = tk.Label(self.root, text="Total Cost:", font=("Arial", 12), bg="#f2f2f2")
        self.total_cost_label.pack(pady=5, anchor="w", padx=20)
        self.total_cost_value = tk.Label(self.root, text="0.0", font=("Arial", 12, "bold"), bg="#f2f2f2")
        self.total_cost_value.pack(pady=5, padx=20, fill="x")

        # Button to calculate total cost with a color change
        self.calculate_button = tk.Button(self.root, text="Calculate Total Cost", font=("Arial", 12), bg="#FF9800", fg="white", command=self.calculate_total_cost)
        self.calculate_button.pack(pady=15, padx=20, fill="x")

        # Button to save data with a color change
        self.save_button = tk.Button(self.root, text="Save Import", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.save_import)
        self.save_button.pack(pady=10, padx=20, fill="x")

        # Exit Button with red color
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=self.root.quit)
        self.exit_button.pack(pady=10, padx=20, fill="x")

    def calculate_total_cost(self):
        try:
            # Get the values from the entry fields
            quantity = int(self.quantity_entry.get())
            price_per_unit = float(self.price_entry.get())
            total_cost = quantity * price_per_unit
            self.total_cost_value.config(text=str(total_cost))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for Quantity and Price per Unit.")

    def save_import(self):
        # Get values from entry fields
        supplier_id = self.supplier_id_entry.get()
        supplier_name = self.supplier_name_entry.get()
        date = self.date_entry.get()
        quantity = self.quantity_entry.get()
        price_per_unit = self.price_entry.get()

        # Validate inputs
        if not supplier_id or not supplier_name or not date or not quantity or not price_per_unit:
            messagebox.showerror("Missing Data", "Please fill in all fields.")
            return

        try:
            quantity = int(quantity)
            price_per_unit = float(price_per_unit)
            total_cost = quantity * price_per_unit
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity and Price per Unit must be numbers.")
            return

        # Save to database
        try:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO imports1 (supplier_id, supplier_name, date, quantity, price_per_unit, total_cost)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (supplier_id, supplier_name, date, quantity, price_per_unit, total_cost))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Import saved successfully!")
            self.clear_fields()  # Clear the form after saving

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def clear_fields(self):
        # Clear all input fields
        self.supplier_id_entry.delete(0, tk.END)
        self.supplier_name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.total_cost_value.config(text="0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImportsModule(root)
    root.mainloop()
