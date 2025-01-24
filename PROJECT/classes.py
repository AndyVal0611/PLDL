from tkinter import *
from PIL import Image, ImageTk

# Main window
window = Tk()
window.title("User Account Information")
window.geometry("900x425")

# Load profile image
profile_image_path = "C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg"
profile_image = Image.open(profile_image_path)
profile_image = profile_image.resize((120, 120))
profile_photo = ImageTk.PhotoImage(profile_image)

# Create a label for "User Account Information" outside the frame, aligned to the left
user_account_label = Label(window, text="User Account Information", font=("Segoe UI", 18, 'bold'))
user_account_label.place(x=20, y=20)  # Set x and y position for label

# Create the main frame and adjust its position to be higher using x and y
main_frame = Frame(window, bg="light gray")
main_frame.place(x=20, y=150, width=860, height=240)  # Set x, y position and size for the frame

# Create a label for the profile picture (outside the main frame, positioned above the frame)
profile_label = Label(window, image=profile_photo)
profile_label.place(x=36, y=87)  # Position the profile picture with x, y coordinates

# Row 1: First Name, Middle Name, Last Name, Suffix, Department
label1 = Label(main_frame, text="First Name", font=("Segoe UI", 9), bg='lightgray')
label1.place(x=150, y=20)
entry1 = Entry(main_frame, font=("Segoe UI", 9), width=23)  # Adjust width here
entry1.place(x=150, y=40)

label2 = Label(main_frame, text="Middle Name", font=("Segoe UI", 9), bg='lightgray')
label2.place(x=303, y=20)
entry2 = Entry(main_frame, font=("Segoe UI", 9), width=23)  # Adjust width here
entry2.place(x=303, y=40)

label3 = Label(main_frame, text="Last Name", font=("Segoe UI", 9), bg='lightgray')
label3.place(x=458, y=20)
entry3 = Entry(main_frame, font=("Segoe UI", 9), width=23)  # Adjust width here
entry3.place(x=458, y=40)

label4 = Label(main_frame, text="Suffix", font=("Segoe UI", 9), bg='lightgray')
label4.place(x=610, y=20)
entry4 = Entry(main_frame, font=("Segoe UI", 9), width=14)  # Adjust width here
entry4.place(x=610, y=40)

label5 = Label(main_frame, text="Department", font=("Segoe UI", 9), bg='lightgray')
label5.place(x=710, y=20)
entry5 = Entry(main_frame, font=("Segoe UI", 9), width=22)  # Adjust width here
entry5.place(x=710, y=40)

# Row 2: Designation, Username, Password
label6 = Label(main_frame, text="Designation", font=("Segoe UI", 9), bg='lightgray')
label6.place(x=20, y=70)
entry6 = Entry(main_frame, font=("Segoe UI", 9), width=40)  # Adjust width here
entry6.place(x=20, y=90)

label7 = Label(main_frame, text="Username", font=("Segoe UI", 9), bg='lightgray')
label7.place(x=278, y=70)
entry7 = Entry(main_frame, font=("Segoe UI", 9), width=33)  # Adjust width here
entry7.place(x=278, y=90)

label8 = Label(main_frame, text="Password", font=("Segoe UI", 9), bg='lightgray')
label8.place(x=493, y=70)
entry8 = Entry(main_frame, font=("Segoe UI", 9), width=40)  # Adjust width here
entry8.place(x=493, y=90)
entry8.config(show="*")  # To hide password text

# Row 3: Confirm Password, User Type, User Status, Employee Number
label9 = Label(main_frame, text="Confirm Password", font=("Segoe UI", 9), bg='lightgray')
label9.place(x=20, y=120)
entry9 = Entry(main_frame, font=("Segoe UI", 9), width=40)  # Adjust width here
entry9.place(x=20, y=140)
entry9.config(show="*")

label10 = Label(main_frame, text="User Type", font=("Segoe UI", 9), bg='lightgray')
label10.place(x=278, y=120)
entry10 = Entry(main_frame, font=("Segoe UI", 9), width=33)  # Adjust width here
entry10.place(x=278, y=140)

label11 = Label(main_frame, text="User Status", font=("Segoe UI", 9), bg='lightgray')
label11.place(x=493, y=120)
entry11 = Entry(main_frame, font=("Segoe UI", 9), width=28)  # Adjust width here
entry11.place(x=493, y=140)

label12 = Label(main_frame, text="Employee Number", font=("Segoe UI", 9), bg='lightgray')
label12.place(x=678, y=120)
entry12 = Entry(main_frame, font=("Segoe UI", 9), width=27)  # Adjust width here
entry12.place(x=678, y=140)

# Buttons
update_button = Button(main_frame, text="Update", bg="blue", fg="white", font=("Segoe UI", 10))
update_button.place(x=269, y=180, width=100)

delete_button = Button(main_frame, text="Delete", bg="yellow", font=("Segoe UI", 10))
delete_button.place(x=380, y=180, width=100)

cancel_button = Button(main_frame, text="Cancel", font=("Segoe UI", 10))
cancel_button.place(x=490, y=180, width=100)

# Runs the code
window.mainloop()