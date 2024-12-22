import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Meralco Bill Form')
root.geometry('650x1033')

# Create a class for the overall GUI Design
class DesignGUI:
    def __init__(self):
        image1 = ''

    def label(self, text, x, y, font=('Arial', 10), width=None, anchor='w', fg_color='black', bg_color=None):
        lbl = tk.Label(root, text=text, font=font, anchor=anchor, fg=fg_color, bg=bg_color if bg_color else root.cget('background'))
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = tk.Entry(root, width=width, font=('Arial', 10))
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=7, command=None):
        btn = tk.Button(root, text=text, width=width, command=command, font=('Arial', 10, 'bold'), bg='#d44713', fg='white')
        btn.place(x=x, y=y)

    def separator(self, x, y, width=610):
        line = tk.Canvas(root, width=width, height=2, bg='black', bd=0, highlightthickness=0)
        line.place(x=x, y=y)

    def set_logo_and_header(self, x, y, logo_path):
        try:
            # Load the image
            img = Image.open(logo_path)
            img = img.resize((70, 70), Image.Resampling.LANCZOS)  # Resize to a smaller size (e.g., 50x50)
            logo_img = ImageTk.PhotoImage(img)

            # Add the image
            logo_label = tk.Label(root, image=logo_img, bg='#f8f8f8')
            logo_label.image = logo_img  # Keep a reference to prevent garbage collection
            logo_label.place(x=x, y=y)

            # Add the text fields next to the logo
            self.label('NAME:', 40, 20, font=('Arial', 8, 'bold'))
            self.entry(185, 20, width=30)

            self.label('ADDRESS:', 40, 40, font=('Arial', 8, 'bold'))
            self.entry(185, 40, width=30)

            self.label('CITY/MUNICIPALITY:', 40, 60, font=('Arial', 8, 'bold'))
            self.entry(185, 60, width=30)

            self.label('PROVINCE:', 40, 80, font=('Arial', 8, 'bold'))
            self.entry(185, 80, width=30)

        except Exception as e:
            print('Error loading logo:', e)

design = DesignGUI()

# Set background color
root.config(bg='white')

# Header Section with logo
logo_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\Meralco Logo.png'
design.set_logo_and_header(528, 20, logo_path)

# Adjusting the "ELECTRIC BILL" label to be centered and match separator width
design.label('ELECTRIC BILL', 20, 113, font=('Arial', 16, 'bold'), bg_color='#d44713', fg_color='black', width=610, anchor='center')

# Electric Bill Section
design.label('Customer Account Number (CAN):', 20, 158, font=('Arial', 9))
can = design.entry(240, 158, width=30)
design.label('Due Date:', 20, 188, font=('Arial', 10, 'bold'))
due_date = design.entry(100, 188, width=20)
design.label('Total Amount Due:', 300, 188, font=('Arial', 10, 'bold'))
total_amount_due = design.entry(436, 188, width=20)

design.separator(20, 220)

# Service Info Section
design.label('SERVICE INFO', 20, 230, font=('Arial', 12, 'bold'))

design.label('Service ID Number:', 20, 260, font=('Arial', 9))
service_id = design.entry(300, 260, width=30)
design.label('Rate:', 20, 285, font=('Arial', 9))
rate = design.entry(300, 285, width=30)
design.label('Contact in the name of:', 20, 310, font=('Arial', 9))
contact_name = design.entry(300, 310, width=30)
design.label('Service Address:', 20, 335, font=('Arial', 9))
service_address = design.entry(300, 335, width=30)

design.separator(20, 370)

# Billing Info Section
design.label('BILLING INFO', 20, 380, font=('Arial', 12, 'bold'))

design.label('Bill Date:', 20, 410, font=('Arial', 9))
bill_date = design.entry(300, 410, width=30)
design.label('Meter Reading Date:', 20, 435, font=('Arial', 9))
meter_reading_date = design.entry(300, 435, width=30)
design.label('Bill Period:', 20, 460, font=('Arial', 9))
bill_period = design.entry(300, 460, width=30)
design.label('Total kWh:', 20, 485, font=('Arial', 9))
total_kwh = design.entry(300, 485, width=30)
design.label('Next Meter Reading:', 20, 510, font=('Arial', 9))
next_meter_reading = design.entry(300, 510, width=30)

design.separator(20, 545)

# Bill Computation Summary Section
design.label('BILL COMPUTATION SUMMARY', 20, 555, font=('Arial', 12, 'bold'))

design.label('Remaining Balance from Previous Bill:', 20, 585, font=('Arial', 9))
remaining_balance = design.entry(300, 585, width=30)
design.label('Charges for this Billing Period:', 20, 610, font=('Arial', 9))
charges_billing_period = design.entry(300, 610, width=30)
design.label('Generation:', 20, 635, font=('Arial', 9))
generation = design.entry(300, 635, width=30)
design.label('Transmission:', 20, 660, font=('Arial', 9))
transmission = design.entry(300, 660, width=30)
design.label('System Loss:', 20, 685, font=('Arial', 9))
system_loss = design.entry(300, 685, width=30)
design.label('Distribution (Meralco):', 20, 710, font=('Arial', 9))
distribution = design.entry(300, 710, width=30)
design.label('Subsidies:', 20, 735, font=('Arial', 9))
subsidies = design.entry(300, 735, width=30)
design.label('Government Taxes:', 20, 760, font=('Arial', 9))
government_taxes = design.entry(300, 760, width=30)
design.label('Universal Charges:', 20, 785, font=('Arial', 9))
universal_charges = design.entry(300, 785, width=30)
design.label('FiT-All (Renewable):', 20, 810, font=('Arial', 9))
fit_all = design.entry(300, 810, width=30)
design.label('Applied Credits:', 20, 835, font=('Arial', 9))
applied_credits = design.entry(300, 835, width=30)
design.label('Other Charges:', 20, 860, font=('Arial', 9))
other_charges = design.entry(300, 860, width=30)
design.label('Installment Due:', 20, 885, font=('Arial', 9))
installment_due = design.entry(300, 885, width=30)
design.label('Total Amount Due:', 20, 910, font=('Arial', 9, 'bold'))
total_amount_due = design.entry(300, 910, width=30)

design.separator(20, 945)

# Footer Section
design.label('Please pay at any Meralco Business Center or through any accredited payment partner before the due date.', 28, 955, font=('Arial', 9, 'italic'), anchor='center', fg_color='#a43404')

# Design button
design.button('PRINT', 168, 992, width=15)
design.button('CLOSE', 350, 992, width=15)

# Runs the code
root.mainloop()