import tkinter as tk
from tkinter import messagebox
from ImportsModule import ImportsModule  # Assuming your ImportsModule is named imports.py
from ExportsModule import ExportsModule  # Assuming your ExportsModule is named exports.py
from tkinter import PhotoImage  # For image support in Tkinter
from PIL import Image, ImageTk  # For handling other image formats like .jpg, .jpeg

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cotton Product Inventory Management System")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")  # Set background color for the root window

 
        self.bg_image = Image.open("image.png")  
        self.bg_image = self.bg_image.resize((600, 400), Image.Resampling.LANCZOS)  # Resize image to fit window size
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_image_tk)
        self.bg_label.place(relwidth=1, relheight=1)  # Cover the entire window with the background image

        # Add an Image (Logo) at the top
        self.logo = Image.open("cpi.png")  # Replace with your logo image path
        self.logo = self.logo.resize((150, 150), Image.Resampling.LANCZOS)  # Resize image with LANCZOS resampling
        self.logo_image = ImageTk.PhotoImage(self.logo)

        self.logo_label = tk.Label(self.root, image=self.logo_image, bg="#f0f0f0")
        self.logo_label.pack(pady=20)

        # Title Label with a custom font and color
        self.title_label = tk.Label(self.root, text="Rice Product Inventory Management", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.title_label.pack(fill="both")

        # Home Page Layout Frame
        self.home_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.home_frame.pack(pady=50)

        # Buttons with custom colors and styling
        self.imports_button = tk.Button(self.home_frame, text="Imports", width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12), command=self.open_imports)
        self.imports_button.grid(row=0, column=0, padx=10, pady=10)

        self.exports_button = tk.Button(self.home_frame, text="Exports", width=20, height=2, bg="#2196F3", fg="white", font=("Arial", 12), command=self.open_exports)
        self.exports_button.grid(row=1, column=0, padx=10, pady=10)

        self.inventory_button = tk.Button(self.home_frame, text="Inventory Viewer", width=20, height=2, bg="#FF9800", fg="white", font=("Arial", 12), command=self.open_inventory)
        self.inventory_button.grid(row=2, column=0, padx=10, pady=10)

        # Exit Button with red color
        self.exit_button = tk.Button(self.home_frame, text="Exit", width=20, height=2, bg="#f44336", fg="white", font=("Arial", 12), command=self.root.quit)
        self.exit_button.grid(row=3, column=0, padx=10, pady=10)

    def open_imports(self):
        # Open the Imports Module in a new window
        self.new_window = tk.Toplevel(self.root)  # Create a new window
        self.app = ImportsModule(self.new_window)  # Open the Imports Module in the new window

    def open_exports(self):
        # Open the Exports Module in a new window
        self.new_window = tk.Toplevel(self.root)  # Create a new window
        self.app = ExportsModule(self.new_window)  # Open the Exports Module in the new window

    def open_inventory(self):
        messagebox.showinfo("Inventory Viewer", "Opening Inventory Viewer...") 
        # Open the Inventory Viewer window here

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()
