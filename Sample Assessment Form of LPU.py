import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Initialize the main window
window = tk.Tk()
window.title('Lyceum of the Philippines University Cavite - Assessment Form')
window.geometry('1520x900')

# Load and set the background image
background_image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\LPU Cavite Background.jpg'
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image.resize((1520, 900)))

# Create a label to hold the background image
background_label = Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the header
header = Frame(window, width=1520, height=120, bg='maroon')
header.place(x=0, y=0)


class design_gui_interface:
    def __init__(self):
        image1 = ''

    def frames(self, x, y, width=1420, height=160):
        self.frame = Frame(window, width=width, height=height, border=50, bg='#FF9999')
        self.frame.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.heading = Label(window, text=text_value, fg='white', bg='maroon', font=('Palatino', 28, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(window, width=25, height=1, fg='black', bg='white')
        self.textbox.place(x=x, y=y)
        return self.textbox

    def textbox_design2(self, x, y):
        self.textbox = Text(window, width=31, height=1, fg='black', bg='white', font=('Calibri', 11, 'bold'))
        self.textbox.place(x=x, y=y)
        return self.textbox

    def label_design(self, x, y, text_value):
        self.label = Label(window, text=text_value, bg='#FF9999', font=('Calibri', 10))
        self.label.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(window, width=15, pady=7, text='Choose File', bg='maroon', fg='white', cursor='hand2',
                                    border=0)
        self.upload_button.place(x=x, y=y)
        return self.upload_button

    def image_design(self, image_location, x, y, length, width):
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.image = self.bck_pic  # Prevent garbage collection
        self.lbl.place(x=x, y=y)


# Displaying the frames created
# Instantiation of the class
my_gui_design = design_gui_interface()

# Call frames attribute within the class named as design_gui_interface
# Call for frame 1
my_gui_design.heading_design(450, 20, 'LYCEUM OF THE PHILIPPINES UNIVERSITY')
my_gui_design.frames(55, 220)

# Add 'Cavite Campus' below the main heading, aligned to the left
cavite_label = Label(
    window,
    text='Cavite Campus',
    fg='white',
    bg='maroon',
    font=('Century Gothic', 15)
)
cavite_label.place(x=450, y=70)  # Adjusted x-coordinate to match the heading

# Call for frame 2
my_gui_design.frames(55, 390)

# Call for frame 3
my_gui_design.frames(55, 560)

# Textbox in first frame
firstnametxt = my_gui_design.textbox_design1(440, 262)
middle_nametxt = my_gui_design.textbox_design1(649, 262)
surnametxt = my_gui_design.textbox_design1(858, 262)
suffix_txt = my_gui_design.textbox_design1(1067, 262)
date_of_birthtxt = my_gui_design.textbox_design1(440, 330)
nationalitytxt = my_gui_design.textbox_design1(1067, 330)

# Display in second frame
departmentxt = my_gui_design.textbox_design2(232, 500)
designationtxt = my_gui_design.textbox_design2(495, 500)
employee_statustxt = my_gui_design.textbox_design2(760, 500)
employee_numbertxt = my_gui_design.textbox_design2(1025, 500)
contact_numbertxt = my_gui_design.textbox_design2(232, 435)
email_addresstxt = my_gui_design.textbox_design2(495, 435)
other_social_mediatxt = my_gui_design.textbox_design2(760, 435)
social_media_accounttxt = my_gui_design.textbox_design2(1025, 435)

# Display in third frame
address_line1txt = my_gui_design.textbox_design2(232, 600)
address_line2txt = my_gui_design.textbox_design2(495, 600)
barangaytxt = my_gui_design.textbox_design2(760, 600)
municipalitytxt = my_gui_design.textbox_design2(1025, 600)
province_txt = my_gui_design.textbox_design2(232, 670)
zip_codetxt = my_gui_design.textbox_design2(760, 670)
countrytxt = my_gui_design.textbox_design2(495, 670)
picturepathtxt = my_gui_design.textbox_design2(1025, 670)

# Textbox label for first frame
first_name_lbl = my_gui_design.label_design(440, 235, 'First Name')
middle_name_lbl = my_gui_design.label_design(650, 235, 'Middle Name')
surname_lbl = my_gui_design.label_design(858, 235, 'Surname')
suffix_lbl = my_gui_design.label_design(1067, 235, 'Suffix')
date_of_birth_lbl = my_gui_design.label_design(440, 305, 'Date of Birth')
nationality_lbl = my_gui_design.label_design(1067, 305, 'Nationality')
civil_status_lbl = my_gui_design.label_design(858, 305, 'Civil Status')
gender_lbl = my_gui_design.label_design(650, 305, 'Gender')

# Text label for second frame
program_lbl = my_gui_design.label_design(232, 410, 'Program')
yearlevel_lbl = my_gui_design.label_design(498, 410, 'Year Level')
acad_status_lbl = my_gui_design.label_design(764, 410, 'Academic Status')
enrol_lbl = my_gui_design.label_design(1030, 410, 'Enrolment Status')
emp_contact_num_lbl = my_gui_design.label_design(232, 475, 'Contact Number')
emp_email_add_lbl = my_gui_design.label_design(498, 475, 'Email Address')
emp_social_media_account_lbl = my_gui_design.label_design(764, 475, 'Social Media Account')
emp_social_media_account_lbl = my_gui_design.label_design(1030, 475, 'Social Media Account')

# Text label for third frame
mothersname_lbl = my_gui_design.label_design(232, 575, 'Mother Name')
contactno1_lbl = my_gui_design.label_design(495, 575, 'Contact Number')
occupation1_lbl = my_gui_design.label_design(760, 575, 'Occupation')
emailaddress1_lbl = my_gui_design.label_design(1025, 575, 'Email Address')
fathersname_lbl = my_gui_design.label_design(232, 645, 'Father Name')
contactno2_lbl = my_gui_design.label_design(498, 645, 'Contact Number')
occupation2_lbl = my_gui_design.label_design(764, 645, 'Occupation')
emailaddress2_lbl = my_gui_design.label_design(1024, 645, 'Email Address')

# Combobox creation
combo_field = ttk.Combobox(window, width=30)
combo_field['values'] = ('Female', 'Male', 'Unidentified')
combo_field.place(x=649, y=330)
combo_field.current()

# Adding combobox for civil status
combo_field1 = ttk.Combobox(window, width=30)
combo_field1['values'] = ('Single', 'Married', 'Widow', 'Legally Separated', 'Annulled')
combo_field1.place(x=858, y=330)
combo_field1.current()

# Call image to display
uploaded_image = my_gui_design.image_design('C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\Profile.jpg', 215, 110, 180, 180)

# Call for the button and place it under the image
upload_button = my_gui_design.button_design(255, 300)

# Run the application
window.mainloop()