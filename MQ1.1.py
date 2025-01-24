import MQ1

#Get the input of the consumer.
class Biller_Input:

    def get_biller_input(self):
        obj = MQ1.Consumer_Info()
        print("| Consumer Information |")
        name = input("Consumer's Name: ")
        number = int(input("Consumer's Account Number: "))
        street = input("Consumer's Street: ")
        barangay = input("Consumer's Barangay: ")
        city = input("Consumer's City: ")
        province = input("Consumer's Province: ")

        obj2 = MQ1.Billing_Information()
        print("| Billing Information |")
        rate = float(input("Rate: "))
        kwh = float(input("Total KwH: "))
        previous_bill = float(input("Previous Balance: "))
        generation = float(input("Generation: "))
        transmission = float(input("Transmission: "))
        system_loss = float(input("System Loss: "))
        distribution = float(input("Distribution: "))
        subsidies = float(input("Subsidies: "))
        government_taxes = float(input("Government Taxes: "))
        universal_charges = float(input("Universal Charges: "))
        fit_all = float(input("FiT-All (Renewable): "))
        applied_charges = float(input("Applied Charges: "))
        other_charges = float(input("Other Charges: "))
        installment_due = float(input("Installment Due: "))
        bill_date = input("Bill Date: ")
        billing_period = input("Billing Period: ")
        meter_date = input("Meter Date: ")
        next_meter_date = input("Next Meter Date: ")

        consumer_data = obj.consumer_data(name, number, street, barangay, city, province)
        obj.display_consumer_info()

        consumer_data2 = obj2.consumer_information(name, number, street, barangay, city, province)

        billing_info = obj2.get_billing_info(rate, kwh, previous_bill, generation, transmission, system_loss,
                                             distribution, subsidies, government_taxes, universal_charges, fit_all,
                                             applied_charges, other_charges, installment_due, bill_date, billing_period,
                                             meter_date, next_meter_date)
        obj2.display_billing_info()

#Runs the code.
biller_input = Biller_Input()
biller_input.get_biller_input()