import ME1
#Provide the inputs needed
class Service_information:
    def get_service_information(self):
        #inputs all the data
        obj = ME1.Service_information()
        print("\tSERVICE INFORMATION")
        can = int(input("Contract Number: "))
        account_name = input("Account Name: ")
        service_address = input("Service Address: ")
        tin = input("TIN Number: ")
        rate_class = input("Rate Class: ")
        business_area = input("Business Area: ")

        obj2 = ME1.Metering_Billing_information()
        print("\tMETERING INFORMATION")
        meter_number = input("Meter Number: ")
        mru_no = int(input("MRU No.: "))
        seq_no = input("Sequence Number: ")
        reading_date = input("Reading Date: ")
        present_reading = int(input("Present Reading: "))
        previous_reading = int(input("Previous Reading: "))
        consumption_cubic_meter = int(input("Consumption: "))

        obj3 = ME1.Billing_Summary_information()
        print("\tBILLING SUMMARY")
        msc = float(input("Maintenance Service Charge (MSC): "))
        payment_due_date = input("Payment Due Date: ")

        # Returns input back to the main class.
        get_service_information = obj.get_service_information(can, account_name, service_address, tin,
                                                          rate_class, business_area)

        get_metering_information = obj2.get_metering_information(meter_number, mru_no, seq_no, reading_date,
                                                             present_reading, previous_reading, consumption_cubic_meter)

        ccm = obj3.ccm(consumption_cubic_meter, payment_due_date, msc)

        # Displays all the output.
        obj.display_service_information()
        obj2.display_metering_information()
        obj3.display_billing_summary()

a = Service_information()
a.get_service_information()