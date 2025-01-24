import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Main window
window = tk.Tk()
window.title("Se-ri's Payroll Form")
window.geometry('855x969')
window.configure(bg='#edecea')

# Create a class for the overall GUI
class DesignGUI:
    def __init__(self):
        image1 = ''

    def label(self, text, x, y, font=('Segoe UI', 10), width=None, bg_color='#edecea', fg_color=None, anchor=None):
        lbl = Label(window, text=text, font=font, bg=bg_color, fg=fg_color, anchor=anchor)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = Entry(window, width=width)
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg='light gray', fg='white'):
        btn = Button(window, text=text, width=width, command=command, font=('Segoe UI', 7, 'bold'), bg=bg, fg=fg)
        btn.place(x=x, y=y)

    def frame(self, x, y, w, h):
        frame = Frame(window, width=w, height=h, bg='#f6f6f6')
        frame.place(x=x, y=y)
        return frame

    def add_image(self, x, y, image_path, width=100, height=100):
        # Open image using PIL
        img = Image.open(image_path)
        img = img.resize((width, height))  # Resize image to fit the frame
        photo = ImageTk.PhotoImage(img)

        # Label to display the image
        label = Label(window, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.place(x=x, y=y)

# Instantiation for DesignGUI
design = DesignGUI()

# Header Section with frame and background color
header_frame = design.frame(0, 0, 855, 100)

# Header Section with logo and color modifications
design.label("SE-RI'S PAYROLL CHOICE", 172, 25, font=('Algerian', 33, 'bold'), bg_color='#f6f6f6')

# Employee Basic Info
design.label('EMPLOYEE BASIC INFO', 40, 130, font=('Segoe UI', 12, 'bold'))

# Attach the profile image
image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg'
design.add_image(65, 160, image_path)

# Basic Info Fields
# Left Side
design.label('Employee Number:', 65, 270)
employee_number = design.entry(220, 270, width=27)
design.label('Search Employee:', 65, 300)
design.button('SEARCH', 220, 300, width=16, bg='red', fg='white')
design.label('Department:', 65, 330)
department = design.entry(220, 330, width=27)

# The remaining details will be transferred on the right side of Basic Info Fields
fields_right = [
    ('First Name:', 140),
    ('Middle Name:', 170),
    ('Surname:', 200),
    ('Civil Status:', 230),
    ('Qualified Dependents:', 260),
    ('Pay Date:', 290),
    ('Employee Status:', 320),
    ('Designation:', 350),
]

for label, y in fields_right:
    design.label(label, 470, y)
    design.entry(640, y, width=27)

# Income Sections on the left side
income_sections = [
    ('BASIC INCOME', 390),
    ('Rate / Hour:', 420),
    ('No. of Hours / Cut Off:', 450),
    ('Income / Cut Off:', 480),

    ('HONORARIUM INCOME', 540),
    ('Rate / Hour:', 570),
    ('No. of Hours / Cut Off:', 600),
    ('Income / Cut Off:', 630),

    ('OTHER INCOME', 690),
    ('Rate / Hour:', 720),
    ('No. of Hours / Cut Off:', 750),
    ('Income / Cut Off:', 780),

    ('SUMMARY INCOME', 840),
    ('Gross Income:', 870),
    ('Net Income:', 900)
]

# Create labels and entry fields for income sections
for label, y in income_sections:
    if 'INCOME' in label or 'SUMMARY INCOME' in label:
        design.label(label, 50, y, font=('Segoe UI', 12, 'bold'))
    else:
        design.label(label, 65, y)
        design.entry(220, y, width=27)

# Deduction Sections
# Right side
deduction_start_y = 415
deduction_sections = [
    ('REGULAR DEDUCTIONS', deduction_start_y),
    ('SSS Contribution:', deduction_start_y + 30),
    ('PhilHealth Contribution:', deduction_start_y + 60),
    ('Pag-IBIG Contribution:', deduction_start_y + 90),
    ('Income Tax Contribution:', deduction_start_y + 120),

    ('OTHER DEDUCTIONS', deduction_start_y + 175),
    ('SSS Loan:', deduction_start_y + 205),
    ('Pag-IBIG Loan:', deduction_start_y + 235),
    ('Faculty Savings Deposit:', deduction_start_y + 265),
    ('Faculty Savings Loan:', deduction_start_y + 295),
    ('Salary Loan:', deduction_start_y + 325),
    ('Other Loans:', deduction_start_y + 355),

    ('DEDUCTION SUMMARY', deduction_start_y + 410),
    ('Total Deductions:', deduction_start_y + 440)
]

# Create labels and entry sections for deduction
for label, y in deduction_sections:
    if 'DEDUCTIONS' in label or 'DEDUCTION SUMMARY' in label:
        design.label(label, 455, y, font=('Segoe UI', 12, 'bold'))
    else:
        design.label(label, 470, y)
        design.entry(640, y, width=27)

# Buttons inside the frame
design.button('GROSS INCOME', 455, 900, width=13, bg='#1379ab', fg='white')
design.button('NET INCOME', 542, 900, width=13, bg='#1379ab', fg='white')
design.button('SAVE', 630, 900, width=8, bg='#13abab', fg='white')
design.button('UPDATE', 692, 900, width=8, bg='#13abab', fg='white')
design.button('NEW', 755, 900, width=8, bg='#edd324', fg='black')

# Runs the code
window.mainloop()