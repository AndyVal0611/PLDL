import tkinter as tk
from tkinter import ttk

class UserFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Form")
        self.root.geometry("900x350")
        self.root.configure(bg="white")

        # Set font to Segoe UI
        self.font = ("Segoe UI", 10)

        # Add profile picture placeholder
        self.photo = tk.Label(root, text="Profile\nPhoto", bg="lightgray", width=15, height=7, relief="groove", font=self.font)
        self.photo.grid(row=0, column=0, rowspan=3, padx=(30, 10), pady=(20, 10), sticky=tk.W)

        # Add labels and entry widgets for user details
        self.create_label_entry("First Name", 3, 1)
        self.create_label_entry("Middle Name", 3, 2)
        self.create_label_entry("Last Name", 3, 5)
        self.create_label_entry("Suffix", 3, 7)
        self.create_label_entry("Department", 3, 7)

        self.create_label_entry("Designation", 5, 1, width=20)
        self.create_label_entry("Username", 5, 2)
        self.create_label_entry("Password", 5, 3, show="*")
        self.create_label_entry("Confirm Password", 5, 4, show="*", width=20)

        self.create_label_entry("User Type", 6, 1)
        self.create_label_entry("User Status", 6, 2)
        self.create_label_entry("Employee Number", 6, 3)

        self.update_button = tk.Button(root, text="Update", bg="blue", fg="white", width=10, font=self.font)
        self.update_button.grid(row=50, column=1, pady=40, padx=(5, 10))

        self.delete_button = tk.Button(root, text="Delete", bg="yellow", fg="black", width=10, font=self.font)
        self.delete_button.grid(row=50, column=2, pady=40, padx=5)

        self.cancel_button = tk.Button(root, text="Cancel", bg="lightgray", fg="black", width=10, font=self.font)
        self.cancel_button.grid(row=50, column=3, pady=40, padx=5)

    def create_label_entry(self, label_text, row, col, **kwargs):
        label = tk.Label(self.root, text=label_text, bg="white", font=self.font)
        label.grid(row=row, column=col, padx=5, pady=5, sticky=tk.E)
        entry = ttk.Entry(self.root, font=self.font, **kwargs)
        entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky=tk.W)
        setattr(self, f"{label_text.replace(' ', '_').lower()}_entry", entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserFormApp(root)
    root.mainloop()
