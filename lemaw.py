import tkinter as tk
from huh import DesignGUI

# Main window
window = tk.Tk()
window.title("SE-RI'S CHOICE PAYROLL")
window.geometry("900x1000")
window.resizable(False, False)

# Instantiate the design class
design = DesignGUI(window)

# Header
design.label("SE-RI'S CHOICE PAYROLL", 300, 20, font=("Arial", 16, "bold"), fg="#8B1C62")

# Employee Basic Info
design.label("EMPLOYEE BASIC INFO:", 20, 60, font=("Arial", 12, "bold"), fg="#8B1C62")

# Image frame for employee picture
image_frame = design.frame(20, 100, 100, 100)
design.label("Image", 35, 140, font=("Arial", 10), width=50)


image_path = ("C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\Profile.jpg")
design.add_image(20, 100, image_path)


design.label("Employee Number:", 130, 110, fg="#6E2C65")
employee_number = design.entry(250, 110)
design.label("Search Employee:", 130, 140, fg="#6E2C65")
search_entry = design.entry(250, 140)

design.button("SEARCH", 20, 240, width=15, bg="#FF69B4", fg="white")

design.label("Department:", 130, 170, fg="#6E2C65")
department = design.entry(250, 170)

fields_right = [
    ("Firstname:", 100),
    ("Middlename:", 130),
    ("Surname:", 160),
    ("Civil Status:", 190),
    ("Qualified Dependents:", 220),
    ("Paydate:", 250),
    ("Employee Status:", 280),
    ("Designation:", 310),
]

for label, y in fields_right:
    design.label(label, 400, y, fg="#6E2C65")
    design.entry(550, y, width=25)

income_sections = [
    ("BASIC INCOME", 350),
    ("Rate / Hour:", 380),
    ("No. of Hours / Cut Off:", 410),
    ("Income / Cut Off:", 440),
    ("HONORARIUM INCOME", 470),
    ("Rate / Hour:", 500),
    ("No. of Hours / Cut Off:", 530),
    ("Income / Cut Off:", 560),
    ("OTHER INCOME", 590),
    ("Rate / Hour:", 620),
    ("No. of Hours / Cut Off:", 650),
    ("Income / Cut Off:", 680),
]

for label, y in income_sections:
    if "INCOME" in label:
        design.label(label, 20, y, font=("Arial", 12, "bold"), fg="#8B1C62")
    else:
        design.label(label, 20, y, fg="#6E2C65")
        design.entry(180, y)

deduction_start_y = 340

# Deductions Section
deduction_sections = [
    ("REGULAR DEDUCTIONS", deduction_start_y),
    ("SSS Contribution:", deduction_start_y + 30),
    ("PhilHealth Contribution:", deduction_start_y + 60),
    ("Pagibig Contribution:", deduction_start_y + 90),
    ("OTHER DEDUCTIONS", deduction_start_y + 120),
    ("SSS Loan:", deduction_start_y + 150),
    ("Pagibig Loan:", deduction_start_y + 180),
    ("Other Loan:", deduction_start_y + 210),
    ("DEDUCTION SUMMARY", deduction_start_y + 240),
    ("Total Deductions:", deduction_start_y + 270),
]

for label, y in deduction_sections:
    if "DEDUCTIONS" in label:
        design.label(label, 400, y, font=("Arial", 12, "bold"), fg="#8B1C62")
    else:
        design.label(label, 400, y, fg="#6E2C65")
        design.entry(580, y)

design.label("SUMMARY INCOME", 20, 710, font=("Arial", 12, "bold"), fg="#8B1C62")
design.label("Gross Income:", 20, 740, fg="#6E2C65")
design.entry(180, 740)
design.label("Net Income:", 20, 770, fg="#6E2C65")
design.entry(180, 770)

design.label("DEDUCTION SUMMARY", 400, 710, font=("Arial", 12, "bold"), fg="#8B1C62")
design.label("Total Deductions:", 400, 740, fg="#6E2C65")
design.entry(580, 740)

buttons = [
    ("GROSS INCOME", 20, "#FFB6C1"),  # Light pink
    ("NET INCOME", 180, "#FF69B4"),  # Hot pink
    ("SAVE", 360, "#FFB6C1"),  # Light pink
    ("UPDATE", 540, "#FF1493"),  # Deep pink
    ("NEW", 720, "#FF69B4")  # Hot pink
]

for text, x, color in buttons:
    design.button(text, x, 820, width=15, bg=color, fg="black")

window.mainloop()