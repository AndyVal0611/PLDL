import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class MeralcoForm:
    def __init__(self, root):
        self.root = root
        self.root.title("MERALCO Application Form")
        self.root.geometry('1520x900')
        self.root.configure(bg='white')

        # Load and set background image
        self.set_background("C:\\Users\\admin\\PycharmProjects\\LAB 3 FILES - VALDEZ\\PLDL01E - (VALDEZ)\\IMAGES\\Meralco.jpg")

        # Frames and widgets
        self.create_frames()
        self.create_widgets()

    def set_background(self, image_path):
        """Set background image for the form."""
        bg_image = Image.open(image_path)
        bg_resized = bg_image.resize((1520, 900))
        self.bg_photo = ImageTk.PhotoImage(bg_resized)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_frames(self):
        """Create frames for the form sections."""
        self.customer_frame = Frame(self.root, bg='white', width=800, height=250)
        self.customer_frame.place(x=700, y=50)  # Adjusted x position for right alignment

        self.billing_frame = Frame(self.root, bg='white', width=800, height=250)
        self.billing_frame.place(x=700, y=350)  # Adjusted x position for right alignment

        self.payment_frame = Frame(self.root, bg='white', width=800, height=150)
        self.payment_frame.place(x=700, y=650)  # Adjusted x position for right alignment

    def create_widgets(self):
        """Create widgets for customer, billing, and payment sections."""

        # Customer Information
        Label(self.customer_frame, text="Customer Information", font=("Arial", 16, "bold"), bg='white', fg='black').grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.customer_frame, text="Name:", font=("Arial", 12), bg='white').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(self.customer_frame, text="Address:", font=("Arial", 12), bg='white').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        Label(self.customer_frame, text="Contact Number:", font=("Arial", 12), bg='white').grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Label(self.customer_frame, text="Account Number:", font=("Arial", 12), bg='white').grid(row=4, column=0, sticky=W, padx=10, pady=5)

        self.name_txt = Entry(self.customer_frame, font=("Arial", 12), width=40)
        self.name_txt.grid(row=1, column=1, padx=10, pady=5)
        self.address_txt = Entry(self.customer_frame, font=("Arial", 12), width=40)
        self.address_txt.grid(row=2, column=1, padx=10, pady=5)
        self.contact_txt = Entry(self.customer_frame, font=("Arial", 12), width=40)
        self.contact_txt.grid(row=3, column=1, padx=10, pady=5)
        self.account_txt = Entry(self.customer_frame, font=("Arial", 12), width=40)
        self.account_txt.grid(row=4, column=1, padx=10, pady=5)

        # Billing Information
        Label(self.billing_frame, text="Billing Information", font=("Arial", 16, "bold"), bg='white', fg='black').grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.billing_frame, text="Meter Number:", font=("Arial", 12), bg='white').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(self.billing_frame, text="Previous Reading (kWh):", font=("Arial", 12), bg='white').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        Label(self.billing_frame, text="Current Reading (kWh):", font=("Arial", 12), bg='white').grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Label(self.billing_frame, text="Bill Amount (PHP):", font=("Arial", 12), bg='white').grid(row=4, column=0, sticky=W, padx=10, pady=5)

        self.meter_txt = Entry(self.billing_frame, font=("Arial", 12), width=40)
        self.meter_txt.grid(row=1, column=1, padx=10, pady=5)
        self.previous_txt = Entry(self.billing_frame, font=("Arial", 12), width=40)
        self.previous_txt.grid(row=2, column=1, padx=10, pady=5)
        self.current_txt = Entry(self.billing_frame, font=("Arial", 12), width=40)
        self.current_txt.grid(row=3, column=1, padx=10, pady=5)
        self.bill_txt = Entry(self.billing_frame, font=("Arial", 12), width=40)
        self.bill_txt.grid(row=4, column=1, padx=10, pady=5)

        # Payment Information
        Label(self.payment_frame, text="Payment Details", font=("Arial", 16, "bold"), bg='white', fg='black').grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.payment_frame, text="Payment Method:", font=("Arial", 12), bg='white').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(self.payment_frame, text="Amount Paid (PHP):", font=("Arial", 12), bg='white').grid(row=2, column=0, sticky=W, padx=10, pady=5)

        self.payment_combo = ttk.Combobox(self.payment_frame, font=("Arial", 12), width=37)
        self.payment_combo['values'] = ("Cash", "Credit Card", "Online Transfer")
        self.payment_combo.grid(row=1, column=1, padx=10, pady=5)

        self.amount_paid_txt = Entry(self.payment_frame, font=("Arial", 12), width=40)
        self.amount_paid_txt.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.calculate_btn = Button(self.root, text="Calculate Bill", font=("Arial", 12), bg="green", fg="white", command=self.calculate_bill)
        self.calculate_btn.place(x=800, y=820, width=150, height=40)

        self.reset_btn = Button(self.root, text="Reset Form", font=("Arial", 12), bg="red", fg="white", command=self.reset_form)
        self.reset_btn.place(x=1000, y=820, width=150, height=40)

    def calculate_bill(self):
        """Calculate the electricity bill."""
        try:
            current = float(self.current_txt.get())
            previous = float(self.previous_txt.get())
            if current < previous:
                self.bill_txt.delete(0, END)
                self.bill_txt.insert(0, "Error")
            else:
                consumption = current - previous
                rate = 10  # Example rate
                bill = consumption * rate
                self.bill_txt.delete(0, END)
                self.bill_txt.insert(0, f"{bill:.2f}")
        except ValueError:
            self.bill_txt.delete(0, END)
            self.bill_txt.insert(0, "Invalid Input")

    def reset_form(self):
        """Reset the form fields."""
        for widget in [self.name_txt, self.address_txt, self.contact_txt, self.account_txt,
                       self.meter_txt, self.previous_txt, self.current_txt, self.bill_txt, self.amount_paid_txt]:
            widget.delete(0, END)
        self.payment_combo.set("")


# Main loop
if __name__ == "__main__":
    root = Tk()
    app = MeralcoForm(root)
    root.mainloop()
