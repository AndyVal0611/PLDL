from tkinter import *
from PIL import Image, ImageTk
from UserAccountClasses import UserAccountApp

# Initialize the main window (this is the correct way to create the Tkinter window)
window = Tk()
window.title("User Account Information")
window.geometry("900x425")

# Load profile image
profile_image_path = "C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg"
profile_image = Image.open(profile_image_path)
profile_image = profile_image.resize((120, 120))
profile_photo = ImageTk.PhotoImage(profile_image)

# Create and instantiate the UserAccountApp class
app = UserAccountApp(window)

app.first_name = app.create_label_entry("First Name", 150, 20)
app.middle_name = app.create_label_entry("Middle Name", 303, 20)
app.last_name = app.create_label_entry("Last Name", 458, 20)
app.suffix = app.create_label_entry("Suffix", 610, 20, width=14)
app.department = app.create_label_entry("Department", 710, 20, width=22)

app.designation = app.create_label_entry("Designation", 20, 70, width=40)
app.username = app.create_label_entry("Username", 278, 70, width=33)
app.password = app.create_label_entry("Password", 493, 70, width=40, show="*")

app.confirm_password = app.create_label_entry("Confirm Password", 20, 120, width=40, show="*")
app.user_type = app.create_label_entry("User Type", 278, 120, width=33)
app.user_status = app.create_label_entry("User Status", 493, 120, width=28)
app.employee_number = app.create_label_entry("Employee Number", 678, 120, width=27)

# Create the profile picture
profile_label = Label(window, image=profile_photo)
profile_label.place(x=36, y=87)

# Run the application
window.mainloop()
