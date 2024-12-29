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

# Create the profile picture
profile_label = Label(window, image=profile_photo)
profile_label.place(x=36, y=87)

# Run the application
window.mainloop()
