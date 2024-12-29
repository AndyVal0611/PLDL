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

        # Initialize labels and textboxes
        self.first_name = self.create_label_entry("First Name", 150, 20)
        self.middle_name = self.create_label_entry("Middle Name", 303, 20)
        self.last_name = self.create_label_entry("Last Name", 458, 20)
        self.suffix = self.create_label_entry("Suffix", 610, 20, width=14)
        self.department = self.create_label_entry("Department", 710, 20, width=22)

        self.designation = self.create_label_entry("Designation", 20, 70, width=40)
        self.username = self.create_label_entry("Username", 278, 70, width=33)
        self.password = self.create_label_entry("Password", 493, 70, width=40, show="*")

        self.confirm_password = self.create_label_entry("Confirm Password", 20, 120, width=40, show="*")
        self.user_type = self.create_label_entry("User Type", 278, 120, width=33)
        self.user_status = self.create_label_entry("User Status", 493, 120, width=28)
        self.employee_number = self.create_label_entry("Employee Number", 678, 120, width=27)

        # Buttons
        self.create_buttons()

    def create_user_account_label(self):
        self.user_account_label = Label(self.window, text="User Account Information", font=("Segoe UI", 18, 'bold'))
        self.user_account_label.place(x=20, y=20)

    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg="light gray")
        self.main_frame.place(x=20, y=150, width=860, height=240)

    def create_label_entry(self, label_text, x, y, width=23, show=None):
        label = Label(self.main_frame, text=label_text, font=("Segoe UI", 9), bg='light gray')
        label.place(x=x, y=y)
        entry = Entry(self.main_frame, font=("Segoe UI", 9), width=width)
        entry.place(x=x, y=y + 20)
        if show:
            entry.config(show=show)
        return entry

    def create_buttons(self):
        self.update_button = Button(self.main_frame, text="Update", bg="blue", fg="white", font=("Segoe UI", 9))
        self.update_button.place(x=269, y=180, width=100)

        self.delete_button = Button(self.main_frame, text="Delete", bg="yellow", font=("Segoe UI", 9))
        self.delete_button.place(x=380, y=180, width=100)

        self.cancel_button = Button(self.main_frame, text="Cancel", font=("Segoe UI", 9))
        self.cancel_button.place(x=490, y=180, width=100)