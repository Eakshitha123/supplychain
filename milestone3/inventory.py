import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import font

class InventoryViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Viewer")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f0f0")  # Set background color for the root window

        # Custom font for labels and buttons
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Title Label with a custom font and color
        self.title_label = tk.Label(self.root, text="Current Inventory", font=("Helvetica", 16, "bold"), fg="#4CAF50", bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Frame to hold inventory data
        self.data_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.data_frame.pack(pady=10)

        # Inventory Data Label
        self.inventory_data_label = tk.Label(self.data_frame, text="Loading inventory...", font=self.custom_font, fg="#333")
        self.inventory_data_label.grid(row=0, column=0, padx=10, pady=10)

        # Button to refresh inventory data
        self.refresh_button = tk.Button(self.root, text="Refresh Inventory", font=self.custom_font, bg="#4CAF50", fg="white", command=self.load_inventory_data)
        self.refresh_button.pack(pady=20)

        # Load the inventory data when the app starts
        self.load_inventory_data()

    def load_inventory_data(self):
        try:
            # Connect to the database
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()

            # Query to get the total quantity from imports
            cursor.execute("SELECT SUM(quantity) FROM imports1")
            total_imported = cursor.fetchone()[0] or 0

            # Query to get the total quantity from exports
            cursor.execute("SELECT SUM(quantity) FROM exports1")
            total_exported = cursor.fetchone()[0] or 0

            # Calculate the remaining inventory
            remaining_inventory = total_imported - total_exported

            # Update the label with inventory details
            self.inventory_data_label.config(text=f"Imported: {total_imported}\nExported: {total_exported}\nRemaining: {remaining_inventory}")

            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryViewer(root)
    root.mainloop()
