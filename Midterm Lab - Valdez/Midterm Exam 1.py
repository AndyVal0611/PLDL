# import or call Midterm_Exam

import Midterm_Exam

service_info_obj = Service_information()

can = int(input("CAN: "))
account_name = input("Name: ")
service_address = input("Address: ")
tin = input("TIN: ")
rate_class = input("Rate class: ")
business_area = input("Business area: ")

metering_info_obj = Metering_Billing_information()
meter_no = input("Input No.: ")
mru_no = int(input("MRU No.: "))
seq_no = int(input("SEQ No.: "))
reading_date = int(input("Reading date: "))
present_reading = int(input("Present reading: "))
previous_reading = int(input("Previous reading: "))

consumption = present_reading - previous_reading
print(f"Consumption (cu.m): , {consumption}")

metering_info_obj.get_metering_information(meter_no, mru_no, seq_no, reading_date, present_reading, previous_reading,)

metering_info_obj.display_metering_information()

metering_info_obj.get_billing_summary()

billing_period = int(input("Billing period: "))
msc = int(input("MSC: "))
payment_due_ate = input("Payment due: ")

metering_info_obj.display_billing_summary()















