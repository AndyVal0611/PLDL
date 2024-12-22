import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('LPU Cavite Enrollment Assessment Form')
root.geometry('1190x1040')

# Create a class for the overall GUI
class DesignGUI:
    def label(self, text, x, y, font=('Palatino', 10, 'bold'), width=None, anchor='w'):
        lbl = tk.Label(root, text=text, font=font, anchor=anchor)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = tk.Entry(root, width=width, font=('Palatino', 10))
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg=None, fg=None):
        btn = tk.Button(root, text=text, width=width, command=command, font=('Calibri', 12, 'bold'), bg=bg, fg=fg)
        btn.place(x=x, y=y)

    def separator(self, x, y, width=1150):
        line = tk.Canvas(root, width=width, height=2, bg='black', bd=0, highlightthickness=0)
        line.place(x=x, y=y)

# Instantiation of DesignGUI
design = DesignGUI()

# Function to load and display the logo
def load_logo():
    logo_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\LPU Logo.jpg'
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((80, 80), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(logo_image)

# Header Section
logo = load_logo()
logo_label = tk.Label(root, image=logo, font=('Palatino', 10))
logo_label.place(x=278, y=27)

lyceum_label = tk.Label(root, text='LYCEUM OF THE PHILIPPINES UNIVERSITY', font=('Palatino', 16, 'bold'))
lyceum_label.place(x=382, y=20)
semester_label = tk.Label(root, text='1st Semester, AY 2024-2025', font=('Palatino', 12))
semester_label.place(x=512, y=60)
assessment_label = tk.Label(root, text='ENROLLMENT ASSESSMENT FORM', font=('Palatino', 14))
assessment_label.place(x=447, y=90)

# Student Information Section
design.label('STUDENT NUMBER:', 20, 150)
student_number = design.entry(180, 150, width=40)
design.label('NAME:', 20, 180)
student_name = design.entry(180, 180, width=40)
design.label('COURSE:', 720, 150)
course = design.entry(820, 150, width=40)
design.label('COLLEGE:', 720, 180)
college = design.entry(820, 180, width=40)

# Class Schedule Section
design.label('CLASS SCHEDULE', 20, 230, font=('Palatino', 12, 'bold'))

columns = ['Subject Code', 'Course Description', 'Section', 'Time', 'Days', 'Room', 'Unit']
tree = ttk.Treeview(root, columns=columns, show='headings', height=10)

# Adjusting the column widths
tree.heading('Subject Code', text='Subject Code')
tree.heading('Course Description', text='Course Description')
tree.heading('Section', text='Section')
tree.heading('Time', text='Time')
tree.heading('Days', text='Days')
tree.heading('Room', text='Room')
tree.heading('Unit', text='Unit')

tree.column('Subject Code', width=150, anchor='center')
tree.column('Course Description', width=250, anchor='center')
tree.column('Section', width=250, anchor='center')
tree.column('Time', width=150, anchor='center')
tree.column('Days', width=100, anchor='center')
tree.column('Room', width=150, anchor='center')
tree.column('Unit', width=100, anchor='center')

subjects = [
    ('CFPL01E', 'Computer Fundamentals and Programming', 'CPE 201', '07:00AM-10:00AM', 'M/W', 'C-202', 2),
    ('DMTN01E', 'Discrete Mathematics', 'CPE 201', '02:30PM-05:30PM', 'S', 'L-205', 3),
    ('ECRL01E', 'Electrical Circuits 1', 'CPE 201', '10:00AM-11:30AM', 'M/W', 'L-205', 4),
    ('', '', '', '04:30PM-07:30PM', 'W', 'C-502'),
    ('EECN41E', 'Engineering Economy', 'CPE 201', '02:30PM-05:30PM', 'F', 'L-205', 3),
    ('ELMN01E', 'Electromagnetics', 'CPE 201', '01:00PM-04:00PM', 'M', 'L-205', 4),
    ('ETHN01G', 'Ethics', 'CPE 201', '05:30PM-07:00PM', 'F/S', 'C-601', 3),
    ('MTHN31E', 'Differential Equations', 'CPE 201', '07:00AM-10:00AM', 'F', 'L-205', 3),
    ('PATHFIT3', 'Physical Activities Toward Health-Fit 3', 'CPE 201', '11:00AM-01:00PM', 'F', 'SRDB1', 2),
    ('PLDL01E', 'Programming Logic and Design', 'CPE 201', '07:00AM-01:00PM', 'S', 'C-203', 2),
]

for subject in subjects:
    tree.insert('', 'end', values=subject)

tree.place(x=20, y=260)

# Fees Section
design.label('TOTAL UNITS', 49, 492, font=('Palatino', 10, 'bold'))
design.label('26', 1111, 492, font=('Palatino', 10, 'bold'))
design.label('TUITION FEE', 20, 520, font=('Palatino', 10, 'bold'))
design.label('39,156.00', 950, 520, font=('Palatino', 10))
design.label('TOTAL MISCELLANEOUS FEES', 20, 540, font=('Palatino', 10, 'bold'))
design.label('12,960.00', 950, 540, font=('Palatino', 10))

design.separator(20, 564)   # Separated by using lines to make the form organized

# Laboratory Fees
design.label('LABORATORY AND OTHER FEES', 20, 572, font=('Palatino', 12, 'bold'))

design.label('OTHER FEES', 20, 596, font=('Palatino', 10))
design.label('Exam Booklet', 20, 616, font=('Palatino', 10))
design.label('540.00', 418, 616, font=('Palatino', 10))

design.label('LABORATORY FEES', 590, 596, font=('Palatino', 10))
fees = [
    ('LMS Fee', 540.00),
    ('Computer Laboratory Fee', 3859.00),
    ('Computer Laboratory Fee 2', 7718.00),
    ('Professional Engineering Laboratory Fee', 3716.00),
]

for i, (desc, fee) in enumerate(fees):
    # Format the fee with commas
    formatted_fee = f'{fee:,.2f}'  # Adds commas for thousands
    design.label(desc, 590, 616 + i * 20, font=('Palatino', 10))
    design.label(formatted_fee, 950, 616 + i * 20, font=('Palatino', 10))

design.separator(20, 706)   # Separated by using lines to make the form organized

design.label('TOTAL LABORATORY AND OTHER FEES', 20, 708, font=('Palatino', 12, 'bold'))
design.label('16,819.00', 950, 708, font=('Palatino', 10))

design.separator(20, 733)   # Separated by using lines to make the form organized

# Total Assessment, Additional Charges, and Total Amount Due for the Tuition Fee
design.label('TOTAL ASSESSMENT', 590,740, font=('Palatino', 10, 'bold'))
design.label('68,935.00', 950, 740, font=('Palatino', 10))
design.label('ADD: INSTALLMENT CHARGE', 590, 762, font=('Palatino', 10))
design.label('1,200.00', 950, 762, font=('Palatino', 10))
design.label('TOTAL AMOUNT DUE', 590, 782, font=('Palatino', 10, 'bold'))
design.label('70,135.00', 950, 782, font=('Palatino', 10))

design.separator(20, 803)  # Separated by using lines to make the form organized

# Acknowledgement and its content
design.label('ACKNOWLEDGEMENT (to be signed by student)', 20, 810, font=('Palatino', 9, 'bold'), anchor='w')
design.label('I understand and agree to the following:', 20, 830, font=('Palatino', 9), anchor='w')
design.label('1. That I am considered officially enrolled for the semester only.', 40, 848, font=('Palatino', 9), anchor='w')
design.label('2. That any unpaid balance shall be paid in full, including the applicable penalties, prior to re-enrollment or issuance of any clearance for graduation or transfer credential.', 40, 868, font=('Palatino', 9), anchor='w')
design.label('3. All Fees are subject to audit.', 40, 888, font=('Palatino', 9), anchor='w')

# Signature label
design.label('Signature over Printed Name and Date', 475, 948, font=('Palatino', 10, 'bold'), anchor='w')

# Creating a text box for signature
signature_box = tk.Entry(root, font=('Palatino', 9), width=40)
signature_box.place(x=462, y=925)

# Buttons
design.button('SUBMIT', 407, 995, width=15, bg='green', fg='white')
design.button('CANCEL', 632, 995, width=15, bg='red', fg='white')

# Runs the code
root.mainloop()