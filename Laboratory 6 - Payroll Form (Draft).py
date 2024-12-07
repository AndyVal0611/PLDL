import tkinter as tk
from tkinter import ttk


# Create the main application window
window = tk.Tk()
window.title("SE-RI'S CHOICE PAYROLL")
window.geometry("1200x850")
window.config(bg="white")


# Header Section
header = tk.Label(window, text="SE-RI'S CHOICE PAYROLL", bg="white", fg="black", font=("Arial", 20, "bold"))
header.pack(pady=10)


# Main Frame to hold all the sections
main_frame = tk.Frame(window, bg="white")
main_frame.pack(pady=10, fill="both", expand=True)


# Employee Basic Info Section
basic_info_frame = tk.LabelFrame(main_frame, text="EMPLOYEE BASIC INFO:", bg="white", font=("Arial", 12, "bold"))
basic_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n", columnspan=2)

# Profile Photo Placeholder
photo_label = tk.Label(basic_info_frame, text="Profile Photo", bg="lightgray", width=15, height=8)
photo_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

# Employee Number
employee_number_label = tk.Label(basic_info_frame, text="Employee Number:", bg="white", font=("Arial", 10))
employee_number_label.grid(row=0, column=1, sticky="w", padx=10)
employee_number_entry = tk.Entry(basic_info_frame, font=("Arial", 10), width=20)
employee_number_entry.grid(row=0, column=2, padx=10)

# Search Button
search_button = tk.Button(basic_info_frame, text="SEARCH", bg="red", fg="white", font=("Arial", 10, "bold"), width=10)
search_button.grid(row=0, column=3, padx=10)

# Department
department_label = tk.Label(basic_info_frame, text="Department:", bg="white", font=("Arial", 10))
department_label.grid(row=1, column=1, sticky="w", padx=10)
department_entry = tk.Entry(basic_info_frame, font=("Arial", 10), width=20)
department_entry.grid(row=1, column=2, padx=10)

# Right Column for Employee Info
fields = ["Firstname:", "Middle Name:", "Surname:", "Civil Status:", "Qualified Dependents Status:", "Paydate:",
          "Employee Status:", "Designation:"]
for idx, field in enumerate(fields):
    label = tk.Label(basic_info_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx % 8, column=4, sticky="w", padx=10, pady=3)
    entry = tk.Entry(basic_info_frame, font=("Arial", 10), width=25)
    entry.grid(row=idx % 8, column=5, padx=10, pady=3)


# Basic Income Section
basic_income_frame = tk.LabelFrame(main_frame, text="BASIC INCOME:", bg="white", font=("Arial", 12, "bold"))
basic_income_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

basic_income_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
for idx, field in enumerate(basic_income_fields):
    label = tk.Label(basic_income_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(basic_income_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Honorarium Income Section
honorarium_frame = tk.LabelFrame(main_frame, text="HONORARIUM INCOME:", bg="white", font=("Arial", 12, "bold"))
honorarium_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")

honorarium_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
for idx, field in enumerate(honorarium_fields):
    label = tk.Label(honorarium_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(honorarium_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Other Income Section
other_income_frame = tk.LabelFrame(main_frame, text="OTHER INCOME:", bg="white", font=("Arial", 12, "bold"))
other_income_frame.grid(row=3, column=0, padx=10, pady=10, sticky="n")

other_income_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
for idx, field in enumerate(other_income_fields):
    label = tk.Label(other_income_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(other_income_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Deductions Section
deductions_frame = tk.LabelFrame(main_frame, text="REGULAR DEDUCTIONS:", bg="white", font=("Arial", 12, "bold"))
deductions_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

deductions_fields = ["SSS Contribution:", "PhilHealth Contribution:", "Pagibig Contribution:", "Income Tax Contribution:"]
for idx, field in enumerate(deductions_fields):
    label = tk.Label(deductions_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(deductions_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Other Deductions Section
other_deductions_frame = tk.LabelFrame(main_frame, text="OTHER DEDUCTIONS:", bg="white", font=("Arial", 12, "bold"))
other_deductions_frame.grid(row=2, column=1, padx=10, pady=10, sticky="n")

other_deductions_fields = ["SSS Loan:", "Pagibig Loan:", "Faculty Savings Deposit:", "Faculty Savings Loan:",
                           "Salary Loan:", "Other Loans:"]
for idx, field in enumerate(other_deductions_fields):
    label = tk.Label(other_deductions_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(other_deductions_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Summary Income Section
summary_frame = tk.LabelFrame(main_frame, text="SUMMARY INCOME:", bg="white", font=("Arial", 12, "bold"))
summary_frame.grid(row=3, column=1, padx=10, pady=10, sticky="n")

summary_fields = ["Gross Income:", "Net Income:"]
for idx, field in enumerate(summary_fields):
    label = tk.Label(summary_frame, text=field, bg="white", font=("Arial", 10))
    label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(summary_frame, width=25, font=("Arial", 10))
    entry.grid(row=idx, column=1, padx=10, pady=5)


# Buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=10)

buttons = ["GROSS INCOME", "NET INCOME", "SAVE", "UPDATE", "NEW"]
for button in buttons:
    btn = tk.Button(button_frame, text=button, bg="#57a1f8", fg="white", font=("Arial", 10, "bold"), width=15)
    btn.pack(side="left", padx=10)

# Run the application
window.mainloop()