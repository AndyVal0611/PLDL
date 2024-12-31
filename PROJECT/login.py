import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title('AV Log-in Page')
window.geometry('1490x900')

# Load and display background image
background_image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\AV Log-in Page.png'
image = Image.open(background_image_path)
bck_pic = ImageTk.PhotoImage(image.resize((1490, 900)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y=1)

# Load and display logo
logo_image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\AV Logo.png'
logo_image = Image.open(logo_image_path)
logo_pic = ImageTk.PhotoImage(logo_image.resize((200, 120)))  # Adjust size as needed
logo_label = Label(window, image=logo_pic, bg='#F9EDED')
logo_label.place(x=648, y=195)  # Position the logo in the middle at the top

# Outer frame (acts as the border)
border_frame = Frame(window, width=414, height=227, bg='#7A0E0E')  # Border color and size
border_frame.place(x=530, y=380)  # Manually placed at the center

# Inner frame (actual content)
frame = Frame(border_frame, width=407, height=220, bg='#F9EDED')  # Content area
frame.place(x=3, y=3)  # Placed slightly inside the border

# Heading Label
heading = Label(text='Welcome Back', fg='#7A0E0E', bg='#F9EDED', font=('Century Gothic', 24, 'bold'))
heading.place(x=620, y=323)

# E-mail Address Label Section
email_label = Label(text='E-mail Address/Username/Phone No.', fg='#7A0E0E', bg='#F9EDED', font=('Century Gothic', 11))
email_label.place(x=550, y=392)
email_textbox = Entry(width=41, fg='#7A0E0E', bg='#F4D2D2', font=('Century Gothic', 12))
email_textbox.place(x=550, y=427)  # Adjusted position to place it below the "E-mail Address" label

# Password Label Section
password_label = Label(text='Password', fg='#7A0E0E', bg='#F9EDED', font=('Century Gothic', 11))
password_label.place(x=550, y=465)
password_textbox = Entry(width=41, fg='#7A0E0E', bg='#F4D2D2', font=('Century Gothic', 12), show='*')
password_textbox.place(x=550, y=500)

# "Forgot Password?" Label
forgot_password = Label(text='Forgot Password?', fg='#7A0E0E', bg='#F9EDED', cursor='hand2', font=('Century Gothic', 8, 'underline'))
forgot_password.place(x=549, y=530)

# Buttons
label = Label(text="Don't have an account?", fg='#7A0E0E', bg='#F9EDED', font=('Century Gothic', 9, 'bold'))
label.place(x=570, y=570)
label = Label(text="Sign-up", fg='#7A0E0E', bg='#F9EDED', cursor='hand2', font=('Century Gothic', 9, 'bold'))
label.place(x=845, y=570)

# Login Button
Button(width=10, pady=1, text='LOGIN', bg='#7A0E0E', fg='white', cursor='hand2', border=0, font=('Century Gothic', 12, 'bold')).place(x=695, y=620)

# Runs the code
window.mainloop()