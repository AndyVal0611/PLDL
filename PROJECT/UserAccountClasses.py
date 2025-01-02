from tkinter import *

# Create a class for DesignGUI
class DesignGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('User Account Information')  # Set window title
        self.window.geometry('900x425')  # Set window size

    # Define the label, which is the title once the output is shown
    def create_user_account_label(self):
        self.user_account_label = Label(self.window, text='User Account Information', font=('Segoe UI', 18, 'bold'))
        self.user_account_label.place(x=20, y=20)

    # Creating a frame for the rows and buttons
    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg='lightgrey')  # Corrected color
        self.main_frame.place(x=20, y=150, width=860, height=240)

    # Method to create label and entry fields for each row
    def create_label_entry(self, label_text, x, y, width=23, show=None):
        # Create label for each field
        label = Label(self.main_frame, text=label_text, font=('Segoe UI', 9), bg='lightgrey')  # Corrected color
        label.place(x=x, y=y)

        # Create corresponding entry field
        entry = Entry(self.main_frame, font=('Segoe UI', 9), width=width)
        entry.place(x=x, y=y + 20)