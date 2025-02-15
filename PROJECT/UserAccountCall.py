from tkinter import *
from PIL import Image, ImageTk
from UserAccountClasses import DesignGUI
# Initialize the main window and the DesignGUI instance
window = Tk()
app = DesignGUI(window)

# Initialize the elements from DesignGUI
app.create_user_account_label()
app.create_main_frame()

# Create a class that will display the design
class DisplayGUI:
    def profile_image(self):
        # Load profile image
        profile_image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg'
        profile_image = Image.open(profile_image_path)
        profile_image = profile_image.resize((120, 120))
        profile_photo = ImageTk.PhotoImage(profile_image)

        # Create the profile picture
        profile_label = Label(window, image=profile_photo)
        profile_label.place(x=36, y=87)
        profile_label.image = profile_photo  # Keep a reference to the image

    def labels_each_row(self):
        # First row
        app.create_label_entry('First Name', 150, 20)
        app.create_label_entry('Middle Name', 303, 20)
        app.create_label_entry('Last Name', 458, 20)
        app.create_label_entry('Suffix', 610, 20, width=14)
        app.create_label_entry('Department', 710, 20, width=22)

        # Second row
        app.create_label_entry('Designation', 20, 70, width=40)
        app.create_label_entry('Username', 278, 70, width=33)
        app.create_label_entry('Password', 493, 70, width=40, show='*')

        # Third row
        app.create_label_entry('Confirm Password', 20, 120, width=40, show='*')
        app.create_label_entry('User Type', 278, 120, width=33)
        app.create_label_entry('User Status', 493, 120, width=28)
        app.create_label_entry('Employee Number', 678, 120, width=27)

    def buttons(self):
        # Buttons
        update_button = Button(window, text="Update", width=10, font=('Segoe UI', 9), bg='Blue', fg='white')
        update_button.place(x=269, y=330, width=100)

        delete_button = Button(window, text="Delete", width=10, font=('Segoe UI', 9), bg='Yellow', fg='black')
        delete_button.place(x=380, y=330, width=100)

        cancel_button = Button(window, text="Cancel", width=10, font=('Segoe UI', 9), bg='Light Gray', fg='black')
        cancel_button.place(x=490, y=330, width=100)

# Create an instance of DisplayGUI
user_gui = DisplayGUI()

# Call the methods from the DisplayGUI instance
user_gui.profile_image()
user_gui.labels_each_row()
user_gui.buttons()

# Run the main loop
window.mainloop()