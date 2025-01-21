import tkinter as tk
from tkinter import messagebox
import sqlite3

class ViewInventory:
    def __init__(self, root):
        self.root = root
        self.root.title("View Inventory")
        self.root.geometry("600x400")

        # Title Label
        self.title_label = tk.Label(self.root, text="Inventory List", font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=10)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display inventory
        self.inventory_listbox = tk.Listbox(self.root, width=80, height=15, yscrollcommand=self.scrollbar.set)
        self.inventory_listbox.pack(pady=20)

        self.scrollbar.config(command=self.inventory_listbox.yview)

        # Load inventory data
        self.load_inventory()

    def load_inventory(self):
        try:
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM imports1")  # Fetch all inventory records
            rows = cursor.fetchall()

            # Display the rows in the listbox
            for row in rows:
                self.inventory_listbox.insert(tk.END, row)

            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewInventory(root)
    root.mainloop()
