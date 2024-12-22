import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Main window
window = tk.Tk()
window.title("AV Paper N' Pixels Payroll Form")
window.geometry("855x1080")
window.configure(bg='#ffffef')

# Create a class for the overall GUI Design
class DesignGUI:
    def __init__(self):
        image1 = ''

    def label(self, text, x, y, font=("Segoe UI", 10), width=None, bg_color='#ffffef', fg_color=None, anchor=None):
        lbl = Label(window, text=text, font=font, bg=bg_color, fg=fg_color, anchor=anchor)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = Entry(window, width=width)
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg="light gray", fg="white"):
        btn = Button(window, text=text, width=width, command=command, font=("Tahoma", 8, "bold"), bg=bg, fg=fg)
        btn.place(x=x, y=y)

    def frame(self, x, y, w, h):
        frame = Frame(window, width=w, height=h, bg="#ffe99e")
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
design.label("AV Paper N' Pixels", 295, 15, font=("Century Gothic", 22, "bold"), bg_color="#ffe99e")
design.label("Payroll Form", 370, 55, font=("Century Gothic", 12, "bold"), bg_color="#ffe99e")

# Employee Basic Info
design.label("EMPLOYEE BASIC INFO", 40, 130, font=("Segoe UI", 12, "bold"))

# Attach the profile image
image_path = "C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg"
design.add_image(65, 160, image_path)

# Basic Info Fields
# Left Side
design.label("Employee Number:", 65, 270)
employee_number = design.entry(220, 270, width=27)

design.label("Search Employee:", 65, 300)
design.button("SEARCH", 220, 300, width=16, bg="#822d21", fg="white")

design.label("Department:", 65, 330)
department = design.entry(220, 330, width=27)

# The remaining details will be transferred on the right side of Basic Info Fields
fields_right = [
    ("First Name:", 140),
    ("Middle Name:", 170),
    ("Surname:", 200),
    ("Civil Status:", 230),
    ("Qualified Dependents:", 260),
    ("Pay Date:", 290),
    ("Employee Status:", 320),
    ("Designation:", 350),
]

for label, y in fields_right:
    design.label(label, 470, y)
    design.entry(640, y, width=27)

# Income Sections on the left side
income_sections = [
    ("BASIC INCOME", 390),
    ("Rate / Hour:", 420),
    ("No. of Hours / Cut Off:", 450),
    ("Income / Cut Off:", 480),

    ("HONORARIUM INCOME", 540),
    ("Rate / Hour:", 570),
    ("No. of Hours / Cut Off:", 600),
    ("Income / Cut Off:", 630),

    ("OTHER INCOME", 690),
    ("Rate / Hour:", 720),
    ("No. of Hours / Cut Off:", 750),
    ("Income / Cut Off:", 780),

    ("SUMMARY INCOME", 840),
    ("Gross Income:", 870),
    ("Net Income:", 900)
]

# Create labels and entry fields for income sections
for label, y in income_sections:
    if "INCOME" in label or "SUMMARY INCOME" in label:
        design.label(label, 50, y, font=("Segoe UI", 12, "bold"))
    else:
        design.label(label, 65, y)
        design.entry(220, y, width=27)

# Deduction Sections
# Right side
deduction_start_y = 415
deduction_sections = [
    ("REGULAR DEDUCTIONS", deduction_start_y),
    ("SSS Contribution:", deduction_start_y + 30),
    ("PhilHealth Contribution:", deduction_start_y + 60),
    ("Pag-IBIG Contribution:", deduction_start_y + 90),
    ("Income Tax Contribution:", deduction_start_y + 120),

    ("OTHER DEDUCTIONS", deduction_start_y + 175),
    ("SSS Loan:", deduction_start_y + 205),
    ("Pag-IBIG Loan:", deduction_start_y + 235),
    ("Faculty Savings Deposit:", deduction_start_y + 265),
    ("Faculty Savings Loan:", deduction_start_y + 295),
    ("Salary Loan:", deduction_start_y + 325),
    ("Other Loans:", deduction_start_y + 355),

    ("DEDUCTION SUMMARY", deduction_start_y + 410),
    ("Total Deductions:", deduction_start_y + 440)
]

# Create labels and entry sections for deduction
for label, y in deduction_sections:
    if "DEDUCTIONS" in label or "DEDUCTION SUMMARY" in label:
        design.label(label, 455, y, font=("Segoe UI", 12, "bold"))
    else:
        design.label(label, 470, y)
        design.entry(640, y, width=27)

# Create a bottom frame around the buttons
button_frame = design.frame(0, 960, 855, 100)
# Buttons inside the frame
design.button("GROSS INCOME", 60, 992, width=15, bg="#6d412a", fg="white")
design.button("NET INCOME", 215, 992, width=15, bg="#6d412a", fg="white")
design.button("SAVE", 370, 992, width=15, bg="#470a07", fg="white")
design.button("UPDATE", 525, 992, width=15, bg="#470a07", fg="white")
design.button("NEW", 680, 992, width=15, bg="#922f04", fg="white")

# Runs the code
window.mainloop()import tkinter as tk
from tkinter import ttk

# Main window initialization
window = tk.Tk()
window.title("AV Paper N' Pixels Payroll Form")
window.geometry('845x1040')
window.configure(bg='#ebd469')  # Set background color

class PayrollForm:
    def __init__(self):
        # Header Section
        self.header = tk.Label(window, text="AV Paper N' Pixels", bg='#ebd469', fg='black', font=('Avant Garde', 20, 'bold'))
        self.header.pack(pady=10)

        # Main Frame to hold all the sections
        self.main_frame = tk.Frame(window, bg='light yellow')
        self.main_frame.pack(pady=10, fill='both', expand=True)

        self.create_employee_basic_info_section()
        self.create_basic_income_section()
        self.create_honorarium_income_section()
        self.create_other_income_section()
        self.create_deductions_section()
        self.create_other_deductions_section()
        self.create_summary_income_section()
        self.create_button_section()

    def create_employee_basic_info_section(self):
        # Employee Basic Info Section
        self.basic_info_frame = tk.LabelFrame(self.main_frame, text='EMPLOYEE BASIC INFO:', bg='light yellow', font=('Segoe UI', 12, 'bold'))
        self.basic_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n', columnspan=2)

        # Profile Photo Placeholder
        self.photo_label = tk.Label(self.basic_info_frame, text='Profile Photo', bg='orange', width=15, height=8)
        self.photo_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        # Employee Number
        self.employee_number_label = tk.Label(self.basic_info_frame, text='Employee Number:', bg='light yellow', font=('segoe ui', 10))
        self.employee_number_label.grid(row=0, column=1, sticky='w', padx=10)
        self.employee_number_entry = tk.Entry(self.basic_info_frame, font=('tahoma', 10), width=20)
        self.employee_number_entry.grid(row=0, column=2, padx=10)

        # Search Button
        self.search_label = tk.Label(self.basic_info_frame, text='Search Employee:', bg='light yellow', font=('tahoma', 10))
        self.search_label.grid(row=1, column=1, sticky='w', padx=10)
        self.search_button = tk.Button(self.basic_info_frame, text='SEARCH', bg='#8a6851', fg='white', font=('tahoma', 10, 'bold'), width=10)
        self.search_button.grid(row=1, column=2, padx=10)

        # Department
        self.department_label = tk.Label(self.basic_info_frame, text='Department:', bg='light yellow', font=('tahoma', 10))
        self.department_label.grid(row=2, column=1, sticky='w', padx=10)
        self.department_entry = tk.Entry(self.basic_info_frame, font=('tahoma', 10), width=20)
        self.department_entry.grid(row=2, column=2, padx=10)

        # Right Column for Employee Info
        fields = ['Firstname:', 'Middle Name:', 'Surname:', 'Civil Status:', 'Qualified Dependents Status:', 'Paydate:', 'Employee Status:', 'Designation:']
        for idx, field in enumerate(fields):
            label = tk.Label(self.basic_info_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx % 8, column=4, sticky='w', padx=10, pady=3)
            entry = tk.Entry(self.basic_info_frame, font=('tahoma', 10), width=25)
            entry.grid(row=idx % 8, column=5, padx=10, pady=3)

    def create_basic_income_section(self):
        # Basic Income Section
        self.basic_income_frame = tk.LabelFrame(self.main_frame, text='BASIC INCOME:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.basic_income_frame.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        basic_income_fields = ['Rate / Hour:', 'No. of Hours / Cut Off:', 'Income / Cut Off:']
        for idx, field in enumerate(basic_income_fields):
            label = tk.Label(self.basic_income_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.basic_income_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_honorarium_income_section(self):
        # Honorarium Income Section
        self.honorarium_frame = tk.LabelFrame(self.main_frame, text='HONORARIUM INCOME:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.honorarium_frame.grid(row=2, column=0, padx=10, pady=10, sticky='n')

        honorarium_fields = ['Rate / Hour:', 'No. of Hours / Cut Off:', 'Income / Cut Off:']
        for idx, field in enumerate(honorarium_fields):
            label = tk.Label(self.honorarium_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.honorarium_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_other_income_section(self):
        # Other Income Section
        self.other_income_frame = tk.LabelFrame(self.main_frame, text='OTHER INCOME:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.other_income_frame.grid(row=3, column=0, padx=10, pady=10, sticky='n')

        other_income_fields = ['Rate / Hour:', 'No. of Hours / Cut Off:', 'Income / Cut Off:']
        for idx, field in enumerate(other_income_fields):
            label = tk.Label(self.other_income_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.other_income_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_deductions_section(self):
        # Deductions Section
        self.deductions_frame = tk.LabelFrame(self.main_frame, text='REGULAR DEDUCTIONS:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.deductions_frame.grid(row=1, column=1, padx=10, pady=10, sticky='n')

        deductions_fields = ['SSS Contribution:', 'PhilHealth Contribution:', 'Pagibig Contribution:', 'Income Tax Contribution:']
        for idx, field in enumerate(deductions_fields):
            label = tk.Label(self.deductions_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.deductions_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_other_deductions_section(self):
        # Other Deductions Section
        self.other_deductions_frame = tk.LabelFrame(self.main_frame, text='OTHER DEDUCTIONS:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.other_deductions_frame.grid(row=2, column=1, padx=10, pady=10, sticky='n')

        other_deductions_fields = ['SSS Loan:', 'Pagibig Loan:', 'Faculty Savings Deposit:', 'Faculty Savings Loan:', 'Salary Loan:', 'Other Loans:']
        for idx, field in enumerate(other_deductions_fields):
            label = tk.Label(self.other_deductions_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.other_deductions_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_summary_income_section(self):
        # Summary Income Section
        self.summary_frame = tk.LabelFrame(self.main_frame, text='SUMMARY INCOME:', bg='light yellow', font=('tahoma', 12, 'bold'))
        self.summary_frame.grid(row=3, column=1, padx=10, pady=10, sticky='n')

        summary_fields = ['Gross Income:', 'Net Income:']
        for idx, field in enumerate(summary_fields):
            label = tk.Label(self.summary_frame, text=field, bg='light yellow', font=('tahoma', 10))
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self.summary_frame, width=25, font=('tahoma', 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_button_section(self):
        # Buttons Section for Layout
        self.button_frame = tk.Frame(window, bg='#ebd469')
        self.button_frame.pack(pady=10)

        buttons = ['GROSS INCOME', 'NET INCOME', 'SAVE', 'UPDATE', 'NEW']
        for i, button in enumerate(buttons):
            btn = tk.Button(self.button_frame, text=button, bg='#6d412a' if i < 2 else '#44312b' if i < 4 else '#8f5d46', fg='white', font=('calibri', 10, 'bold'), width=15)
            btn.grid(row=0, column=i, padx=10)  # Use grid() for buttons

# Run the application
app = PayrollForm()
window.mainloop()