#Create two classes that processes the inputs of the consumer.
#1st Class would be to process the consumer's information.
class Consumer_Info:

    #Initialize all of the variables.
    def __init__(self):
        self.biller_name = ""
        self.biller_number = ""
        self.biller_street = ""
        self.biller_baranggay = ""
        self.biller_city = ""
        self.biller_province = ""

    #Define all of the variables from the inputs.
    def consumer_data(self, biller_name, biller_number, biller_street, biller_barangay, biller_city, biller_province):
        self.biller_name = biller_name
        self.biller_number = biller_number
        self.biller_street = biller_street
        self.biller_baranggay = biller_barangay
        self.biller_city = biller_city
        self.biller_province = biller_province

    #Display all of the information from the definition of variables.
    def display_consumer_info(self):
        width = 50
        names = 46
        print("-" * width)
        print(f"| {self.biller_name:<{names}} |")
        print(f"| {self.biller_street:<{names}} |")
        print(f"| {self.biller_baranggay:<{names}} |")
        print(f"| {self.biller_city:<{names}} |")
        print(f"| {self.biller_province:<{names}} |")
        print("-" * width)
        print(f"| Service Info \t\t\t\t\t\t\t\t\t |")
        print("-" * width)
        print(f"| Account Number: {self.biller_number:<{names - 16}} |")

#2nd Class would be to process all of the computations of the consumer.
class Billing_Information:

    # Initialize all of the variables.
    def __init__(self):
        self.rate = 0.00
        self.total_kwh = 0.00
        self.previous_bill = 0.00
        self.generation = 0.00
        self.transmission = 0.00
        self.system_loss = 0.00
        self.distribution = 0.00
        self.subsidies = 0.00
        self.government_taxes = 0.00
        self.universal_charges = 0.00
        self.fit_all = 0.00
        self.applied_charges = 0.00
        self.other_charges = 0.00
        self.installment_due = 0.00
        self.charge_amount = 0.00
        self.total_amount_due = 0.00
        self.previous_bill_output = ""
        self.bill_date = ""
        self.billing_period = ""
        self.meter_date = ""
        self.next_meter_date = ""

    #Process all of the computations.
    def get_billing_info(self, rate, kwh, previous_bill, generation, transmission, system_loss, distribution, subsidies,
                         government_taxes, universal_charges, fit_all,
                         applied_charges, other_charges, installment_due, bill_date, billing_period, meter_date,
                         next_meter_date):
        self.rate = rate
        self.total_kwh = kwh
        self.previous_bill = previous_bill
        self.generation = generation
        self.transmission = transmission
        self.system_loss = system_loss
        self.distribution = distribution
        self.subsidies = subsidies
        self.government_taxes = government_taxes
        self.universal_charges = universal_charges
        self.fit_all = fit_all
        self.applied_charges = applied_charges
        self.other_charges = other_charges
        self.installment_due = installment_due
        self.bill_date = bill_date
        self.billing_period = billing_period
        self.meter_date = meter_date
        self.next_meter_date = next_meter_date

        self.charge_amount = (rate * kwh)

        self.total_amount_due = (
                    previous_bill + generation + transmission + system_loss + distribution + subsidies + government_taxes + universal_charges + fit_all +
                    applied_charges + other_charges + installment_due + self.charge_amount)

        if self.previous_bill == 0:
            self.previous_bill_output = "Thank You!"
        elif self.previous_bill > 0:
            self.previous_bill_output = "Please Pay The Previous Bill."

    # Connect variables.
    def consumer_information(self, name, number, street, barangay, city, province):
        self.biller_name = name
        self.biller_number = number
        self.biller_street = street
        self.biller_barangay = barangay
        self.biller_city = city
        self.biller_province = province

    # Display all of the information.
    def display_billing_info(self):
        width = 50
        names = 46
        print(f"| Rate: {self.rate:<{names - 6}} |")
        print(f"| Consumer Name: {self.biller_name:<{names - 15}} |")
        print(f"| Service Address: {self.biller_street} {self.biller_barangay} {self.biller_city} {self.biller_province}")
        print("-" * width)
        print(f"| Billing Info \t\t\t\t\t\t\t\t\t |")
        print("-" * width)
        print(f"| Bill Date: {self.bill_date}")
        print(f"| Meter Date: {self.billing_period}")
        print(f"| Next Meter Date: {self.next_meter_date}")
        print(f"| Billing Period: {self.billing_period}")
        print("-" * width)
        print(f"| Previous Bill: {self.previous_bill}")
        print(f"| {self.previous_bill_output}")
        print("-" * width)
        print(f"| Amount Charge: {self.charge_amount}")
        print(f"| Generation: {self.generation}")
        print(f"| Transmission: {self.transmission}")
        print(f"| System Loss: {self.system_loss}")
        print(f"| Distribution: {self.distribution}")
        print(f"| Subsidies: {self.subsidies}")
        print(f"| Government Taxes: {self.government_taxes}")
        print(f"| Universal Charges: {self.universal_charges}")
        print(f"| FiT-All (Renewable): {self.fit_all}")
        print(f"| Applied Charges: {self.applied_charges}")
        print(f"| Other Charges: {self.other_charges}")
        print(f"| Installment Due: {self.installment_due}")
        print("-" * width)
        print(f"| Total Amount Due: {self.total_amount_due}")
        print("-" * width)