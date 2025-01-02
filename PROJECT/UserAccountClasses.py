from tkinter import *
from PIL import Image, ImageTk

# Create a class for UserAccountApplication
class UserAccountApplication:
    # Initialize the window
    def __init__(self, window):
        self.window = window
        self.window.title('User Account Information')
        self.window.geometry('900x425')

    # Define the label, which is the title once the output is shown
    def create_user_account_label(self):
        self.user_account_label = Label(self.window, text='User Account Information', font=('Segoe UI', 18, 'bold'))
        self.user_account_label.place(x=20, y=20)

    # Creating a frame for the rows and buttons
    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg='light gray')
        self.main_frame.place(x=20, y=150, width=860, height=240)

    # Placeholder method for labels and entries, to be defined in the second file
    def create_label_entry(self, label_text, x, y, width=23, show=None):
        label = Label(self.main_frame, text=label_text, font=('Segoe UI', 9), bg='light gray')
        label.place(x=x, y=y)
        entry = Entry(self.main_frame, font=('Segoe UI', 9), width=width)
        entry.place(x=x, y=y + 20)
        if show:
            entry.config(show=show)
        return entry