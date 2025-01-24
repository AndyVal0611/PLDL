import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Meralco Bill Receipt")
root.geometry("700x850")
root.resizable(False, False)

class DesignGUI:
    def __init__(self):
        image1 = ''

    def label(self, text, x, y, font=("Arial", 10), width=None, anchor="w", fg_color="black", bg_color=None):
        lbl = tk.Label(root, text=text, font=font, anchor=anchor, fg=fg_color, bg=bg_color if bg_color else root.cget("background"))
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = tk.Entry(root, width=width, font=("Arial", 10))
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None):
        btn = tk.Button(root, text=text, width=width, command=command, font=("Arial", 10, "bold"), bg="#ff7f00", fg="white")
        btn.place(x=x, y=y)

    def separator(self, x, y, width=560):
        line = tk.Canvas(root, width=width, height=2, bg="black", bd=0, highlightthickness=0)
        line.place(x=x, y=y)

    def set_logo(self, x, y):
        logo = tk.Label(root, text="Meralco", font=("Arial", 24, "bold"), fg="orange", bg="#f8f8f8")
        logo.place(x=x, y=y)

design = DesignGUI()

# Set background color
root.config(bg="#f8f8f8")

# Header Section with logo
design.set_logo(220, 20)
design.label("Manila Electric Company", 180, 60, font=("Arial", 14), fg_color="orange")

# Line separator after header
design.separator(20, 90)

# Customer Information Section
design.label("Account Number:", 20, 100, font=("Arial", 12))
account_number = design.entry(160, 100, width=30)

design.label("Customer Name:", 20, 130, font=("Arial", 12))
customer_name = design.entry(160, 130, width=30)

design.label("Address:", 20, 160, font=("Arial", 12))
customer_address = design.entry(160, 160, width=30)

design.label("Billing Period:", 20, 190, font=("Arial", 12))
billing_period = design.entry(160, 190, width=30)

# Line separator after customer info
design.separator(20, 220)

# Meter Reading Section
design.label("Meter Reading", 20, 230, font=("Arial", 12, "bold"))
design.label("Previous Reading:", 20, 260, font=("Arial", 12))
previous_reading = design.entry(160, 260, width=30)

design.label("Current Reading:", 20, 290, font=("Arial", 12))
current_reading = design.entry(160, 290, width=30)

design.label("Total Consumption (kWh):", 20, 320, font=("Arial", 12))
total_consumption = design.entry(160, 320, width=30)

# Line separator after meter reading
design.separator(20, 350)

# Charges Section
design.label("Bill Details", 20, 360, font=("Arial", 12, "bold"))
design.label("Electricity Charge (P):", 20, 390, font=("Arial", 12))
electricity_charge = design.entry(160, 390, width=30)

design.label("Other Charges (P):", 20, 420, font=("Arial", 12))
other_charges = design.entry(160, 420, width=30)

design.label("VAT (12%) (P):", 20, 450, font=("Arial", 12))
vat = design.entry(160, 450, width=30)

design.label("Total Charges (P):", 20, 480, font=("Arial", 12))
total_charges = design.entry(160, 480, width=30)

# Line separator after charges
design.separator(20, 510)

# Payments Section
design.label("Payments", 20, 520, font=("Arial", 12, "bold"))
design.label("Payment Made (P):", 20, 540, font=("Arial", 12))
payment_made = design.entry(160, 540, width=30)

design.label("Previous Balance (P):", 20, 570, font=("Arial", 12))
previous_balance = design.entry(160, 570, width=30)

design.label("Payment Method:", 20, 600, font=("Arial", 12))
payment_method = design.entry(160, 600, width=30)

# Line separator after payments
design.separator(20, 630)

# Total Amount Due Section
design.label("Total Amount Due", 20, 640, font=("Arial", 12, "bold"))
design.label("Total Due (Including VAT) (P):", 20, 670, font=("Arial", 12))
total_due = design.entry(160, 670, width=30)

design.label("Due Date:", 20, 700, font=("Arial", 12))
due_date = design.entry(160, 700, width=30)

# Footer Section
design.separator(20, 730)

design.label("Thank you for paying your bill!", 150, 740, font=("Arial", 10, "italic"), anchor="center", fg_color="orange")
design.label("For inquiries, call 16211 or visit meralco.com.ph", 100, 770, font=("Arial", 10), anchor="center")

# Buttons
buttons = [("PRINT", 20), ("CLOSE", 150)]
for text, x in buttons:
    design.button(text, x, 800, width=12)

root.mainloop()