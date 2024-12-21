import tkinter as tk
from tkinter import ttk

class PayrollForm:
    def __init__(self, window):
        self.window = window
        self.window.title("AV Paper N' Pixels Payroll Form")
        self.window.geometry("1200x850")
        self.window.config(bg="#ebd469")

        # Header Section
        self.header = tk.Label(self.window, text="AV Paper N' Pixels", bg="#ebd469", fg="black", font=("Century Gothic", 20, "bold"))
        self.header.pack(pady=10)

        # Main Frame to hold all the sections
        self.main_frame = tk.Frame(self.window, bg="lightyellow")
        self.main_frame.pack(pady=10, fill="both", expand=True)

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
        self.basic_info_frame = tk.LabelFrame(self.main_frame, text="EMPLOYEE BASIC INFO:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.basic_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n", columnspan=2)

        # Profile Photo Placeholder
        self.photo_label = tk.Label(self.basic_info_frame, text="Profile Photo", bg="orange", width=15, height=8)
        self.photo_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        # Employee Number
        self.employee_number_label = tk.Label(self.basic_info_frame, text="Employee Number:", bg="lightyellow", font=("tahoma", 10))
        self.employee_number_label.grid(row=0, column=1, sticky="w", padx=10)
        self.employee_number_entry = tk.Entry(self.basic_info_frame, font=("tahoma", 10), width=20)
        self.employee_number_entry.grid(row=0, column=2, padx=10)

        # Search Button
        self.search_label = tk.Label(self.basic_info_frame, text="Search Employee:", bg="lightyellow", font=("tahoma", 10))
        self.search_label.grid(row=1, column=1, sticky='w', padx=10)
        self.search_button = tk.Button(self.basic_info_frame, text="SEARCH", bg="#8a6851", fg="white", font=("tahoma", 10, "bold"), width=10)
        self.search_button.grid(row=1, column=2, padx=10)

        # Department
        self.department_label = tk.Label(self.basic_info_frame, text="Department:", bg="lightyellow", font=("tahoma", 10))
        self.department_label.grid(row=2, column=1, sticky="w", padx=10)
        self.department_entry = tk.Entry(self.basic_info_frame, font=("tahoma", 10), width=20)
        self.department_entry.grid(row=2, column=2, padx=10)

        # Right Column for Employee Info
        fields = ["Firstname:", "Middle Name:", "Surname:", "Civil Status:", "Qualified Dependents Status:", "Paydate:", "Employee Status:", "Designation:"]
        for idx, field in enumerate(fields):
            label = tk.Label(self.basic_info_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx % 8, column=4, sticky="w", padx=10, pady=3)
            entry = tk.Entry(self.basic_info_frame, font=("tahoma", 10), width=25)
            entry.grid(row=idx % 8, column=5, padx=10, pady=3)

    def create_basic_income_section(self):
        # Basic Income Section
        self.basic_income_frame = tk.LabelFrame(self.main_frame, text="BASIC INCOME:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.basic_income_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        basic_income_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
        for idx, field in enumerate(basic_income_fields):
            label = tk.Label(self.basic_income_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.basic_income_frame, width=25, font=("tahoma", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_honorarium_income_section(self):
        # Honorarium Income Section
        self.honorarium_frame = tk.LabelFrame(self.main_frame, text="HONORARIUM INCOME:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.honorarium_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")

        honorarium_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
        for idx, field in enumerate(honorarium_fields):
            label = tk.Label(self.honorarium_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.honorarium_frame, width=25, font=("tahoma", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_other_income_section(self):
        # Other Income Section
        self.other_income_frame = tk.LabelFrame(self.main_frame, text="OTHER INCOME:", bg="light yellow", font=("tahoma", 12, "bold"))
        self.other_income_frame.grid(row=3, column=0, padx=10, pady=10, sticky="n")

        other_income_fields = ["Rate / Hour:", "No. of Hours / Cut Off:", "Income / Cut Off:"]
        for idx, field in enumerate(other_income_fields):
            label = tk.Label(self.other_income_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.other_income_frame, width=25, font=("tahoma", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_deductions_section(self):
        # Deductions Section
        self.deductions_frame = tk.LabelFrame(self.main_frame, text="REGULAR DEDUCTIONS:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.deductions_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        deductions_fields = ["SSS Contribution:", "PhilHealth Contribution:", "Pagibig Contribution:", "Income Tax Contribution:"]
        for idx, field in enumerate(deductions_fields):
            label = tk.Label(self.deductions_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.deductions_frame, width=25, font=("tahoma", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_other_deductions_section(self):
        # Other Deductions Section
        self.other_deductions_frame = tk.LabelFrame(self.main_frame, text="OTHER DEDUCTIONS:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.other_deductions_frame.grid(row=2, column=1, padx=10, pady=10, sticky="n")

        other_deductions_fields = ["SSS Loan:", "Pagibig Loan:", "Faculty Savings Deposit:", "Faculty Savings Loan:", "Salary Loan:", "Other Loans:"]
        for idx, field in enumerate(other_deductions_fields):
            label = tk.Label(self.other_deductions_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.other_deductions_frame, width=25, font=("tahoma", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_summary_income_section(self):
        # Summary Income Section
        self.summary_frame = tk.LabelFrame(self.main_frame, text="SUMMARY INCOME:", bg="lightyellow", font=("tahoma", 12, "bold"))
        self.summary_frame.grid(row=3, column=1, padx=10, pady=10, sticky="n")

        summary_fields = ["Gross Income:", "Net Income:"]
        for idx, field in enumerate(summary_fields):
            label = tk.Label(self.summary_frame, text=field, bg="lightyellow", font=("tahoma", 10))
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(self.summary_frame, width=25, font=("tahome", 10))
            entry.grid(row=idx, column=1, padx=10, pady=5)

    def create_button_section(self):
        # Buttons
        self.button_frame = tk.Frame(self.window, bg="#ebd469")
        self.button_frame.pack(pady=10)

        buttons = ["GROSS INCOME", "NET INCOME"]
        for button in buttons:
            btn = tk.Button(self.button_frame, text=button, bg="#6d412a", fg="white", font=("calibri", 10, "bold"), width=15)
            btn.pack(side="left", padx=10)

        buttons = ["SAVE", "UPDATE"]
        for button in buttons:
            btn = tk.Button(self.button_frame, text=button, bg="#44312b", fg="white", font=("calibri", 10, "bold"), width=15)
            btn.pack(side="left", padx=10)

        buttons = ["NEW"]
        for button in buttons:
            btn = tk.Button(self.button_frame, text=button, bg="#8f5d46", fg="white", font=("calibri", 10, "bold"), width=15)
            btn.pack(side="left", padx=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = PayrollForm(window)
    window.mainloop()