# Initializing the personal data
class PersonalInfo:
    def __init__(self):
        self.customer_name = ""
        self.address = ""

    def get_personal_info(self, customer_name, address):
        self.customer.name = customer_name
        self.address = address
    def display_personal_info(self):
        print("Customer Name:", self.customer_name)
        print("Address:", self.address)

# Initialize the electric bill
class ElectricBill:
    def __init__(self):
        self.billing_period = ""
        self.billing_due_date = ""
        self.electric_meter_number = ""
        self.meter_reading = ""
        self.next_meter_reading = ""
        self.current_reading = 0.00
        self.previous_reading = 0.00
        self.customer_type = ""
        self.actual_consumption = 0.00
        self.monthly_residential_rate = 8.59
        self.monthly_commercial_rate = 12.00

    def get_electric_bill_info(self):
        self.billing_period = billing_period
        self.billing_due_date = billing_due
        self.electric_meter_number = electric_number_meter
        self.meter_reading = meter_reading
        self.next_meter_reading = next_read
        self.current_reading = current_read
        self.previous_reading = previous_read
        self.customer_type = customer_type
        self.actual_consumption = actual_consumption
        self.monthly_residential_rate = monthly_residential
        self.monthly_commercial_rate = monthly_commercial

    def display_electric_bill_info(self):
        print("\n\t\tYOUR ELECTRIC BILL")
        print("Billing Period:", self.billing_period)
        print("Due Date:", self.billing_due_date)
        print("Electric Meter Number:", self.electric_meter_number)
        print("Date of Meter Reading:", self.meter_reading)
        print("Date of Next Meter Reading:", self.next_meter_reading)
        print("Current Reading:", self.current_reading, "kWh")
        print("Previous Reading:", self.previous_reading, "kWh")
        print("Customer Type:", self.customer_type)
        print("Actual Consumption:", self.actual_consumption, "kWh")


# Initialize the bill computation summary
class BillComputationSummary:
    def __init__(self):
        self.previous_remaining_balance = float(input("Previous Remaining Balance: "))
        self.generation = float(input("Generation Charge: "))
        self.transmission = float(input("Transmission Charge: "))
        self.system_loss = float(input("System Loss Charge: "))
        self.distribution = float(input("Distribution Charge: "))
        self.subsidies = float(input("Subsidies: "))
        self.government_tax = float(input("Government Tax: "))
        self.universal_charges = float(input("Universal Charges: "))
        self.fitan = float(input("FIT-All (Renewable): "))
        self.applied_credits = float(input("Applied Credits: "))
        self.other_charges = float(input("Other Charges: "))
        self.installment_due = float(input("Installment Due: "))
        self.total_amount_due = 0.00

    def calculate_total_amount_due(self):
        self.total_amount_due = (
            self.previous_remaining_balance + self.generation + self.transmission +
            self.system_loss + self.distribution + self.subsidies + self.government_tax +
            self.universal_charges + self.fitan - self.applied_credits + self.other_charges +
            self.installment_due
        )

    def display_charges_summary(self):
        print("\n\t\tBILL COMPUTATION SUMMARY")
        print("Previous Balance:", self.previous_remaining_balance)
        print("Generation Charge:", self.generation)
        print("Transmission Charge:", self.transmission)
        print("System Loss Charge:", self.system_loss)
        print("Distribution Charge:", self.distribution)
        print("Subsidies:", self.subsidies)
        print("Government Tax:", self.government_tax)
        print("Universal Charges:", self.universal_charges)
        print("FIT-All (Renewable):", self.fitan)
        print("Applied Credits:", self.applied_credits)
        print("Other Charges:", self.other_charges)
        print("Installment Due:", self.installment_due)
        print("\tTotal Amount Due: ₱", self.total_amount_due)


personal_info = PersonalInfo()
electric_bill = ElectricBill()
electric_bill.get_electric_bill_info()
bill_computation = BillComputationSummary()
bill_computation.calculate_total_amount_due()

print("\nPersonal Information:")
personal_info.display_personal_info()

print("\nElectric Bill Information:")
electric_bill.display_electric_bill_info()

print("\nBill Charges Breakdown:")
bill_computation.display_charges_summary()










