from tkinter import *
from PIL import Image, ImageTk

class UserAccountApp:
    def __init__(self, window):
        self.window = window
        self.window.title("User Account Information")
        self.window.geometry("900x425")

        # Initialize UI components
        self.create_user_account_label()
        self.create_main_frame()

        # Create Buttons
        self.create_buttons()

    def create_user_account_label(self):
        self.user_account_label = Label(self.window, text="User Account Information", font=("Segoe UI", 18, 'bold'))
        self.user_account_label.place(x=20, y=20)

    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg="light gray")
        self.main_frame.place(x=20, y=150, width=860, height=240)

    def create_buttons(self):
        self.update_button = Button(self.main_frame, text="Update", bg="blue", fg="white", font=("Segoe UI", 9))
        self.update_button.place(x=269, y=180, width=100)

        self.delete_button = Button(self.main_frame, text="Delete", bg="yellow", font=("Segoe UI", 9))
        self.delete_button.place(x=380, y=180, width=100)

        self.cancel_button = Button(self.main_frame, text="Cancel", font=("Segoe UI", 9))
        self.cancel_button.place(x=490, y=180, width=100)

    # Placeholder method for labels and entries, to be defined in the second file
    def create_label_entry(self, label_text, x, y, width=23, show=None):
        label = Label(self.main_frame, text=label_text, font=("Segoe UI", 9), bg='light gray')
        label.place(x=x, y=y)
        entry = Entry(self.main_frame, font=("Segoe UI", 9), width=width)
        entry.place(x=x, y=y + 20)
        if show:
            entry.config(show=show)
        return entry
