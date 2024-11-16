class Personal_info:
    #initialize the personal info's variables
        def __init__(self):
            self.customer_name = ""
            self.address = ""

#input personal info
        def get_personal_info(self, customer_name, address):
            self.customer.name = customer_name
            self.address = address

#display personal info
        def display_personal_info(self):
            print("Customer Name:", self.customer_name)
            print("Address:", self.address)

class Electric_bill:
    #intialize
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

class Bill_computation_salary:
    def __init__(self):
        self.previous_remaining_balance = 0.00
        self.generation = 0.00
        self.transmission = 0.00
        self.distribution = 0.00
        self.subsidies = 0.00
        self.government_tax = 0.00
        self.universal_charges = 0.00
        self.fitan = 0.00
        self.applied_credits = 0.00
        self.other_charges = 0.00
        self.installment_due = 0.00
        self.total_amount_due = 0.00

        self.total_amount_due = generation + transmission + distribution + subsidies + government_tax
                                + universal_charges
