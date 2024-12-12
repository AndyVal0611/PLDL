class Service_information:
    #initialize the service information data
        def __init__(self):
            #service information data
            self.can = 0
            self.account_name = ""
            self.service_address = ""
            self.tin = ""
            self.rate_class = ""
            self.business_area = ""

        def get_service_information(self, can, account_name, service_address, tin, rate_class, business_area):
            # get the variables for service information
            self.can = can
            self.account_name = account_name
            self.service_address = service_address
            self.tin = tin
            self.rate_class = rate_class
            self.business_area = business_area

        def display_service_information(self):
            # display the first part
            print("Advisory: Check payment WILL NOT BE ACCEPTED without the"
                  "Statement of Account effective October 01, 2019")
            print("-----------------------------------------------------------")
            print("                            Maynilad Water Service, Inc.   ")
            print("                            8390 DR A SANTOS AVE BF HOMES  ")
            print("                            PARAÑAQUE CITY                 ")
            print("                            VAT Red TIN 005-393-442-0000   ")
            print("                            SPM No.:                       ")
            print("                            Machine SN:                    ")
            print("                                                           ")
            print("                                                           ")
            print("SOA  #  00000000003456789012")
            print("                    SERVICE INFORMATION                    ")
            print("Contact Account No.: ", self.can)
            print("Service Address: ", self.service_address)
            print("Account Name   : ", self.account_name)
            print("TIN:  ", self.tin)
            print("Rate Class: ", self.rate_class)
            print("Business Area: ", self.business_area)
            print("-----------------------------------------------------------")

class Metering_Billing_information:
    # initialize the metering and billing information data
        def __init__(self):
            # metering information data
            self.meter_no = ""
            self.mru_no = 0
            self.seq_no = 0
            self.reading_date = ""
            self.present_reading = 0
            self.previous_reading = 0
            self.consumption_cubic_meter = 0

        def get_metering_information(self, meter_no, mru_no, seq_no, reading_date, present_reading, previous_reading, consumption_cubic_meter):
            # get the variables given
            self.meter_no = meter_no
            self.mru_no = mru_no
            self.seq_no = seq_no
            self.reading_date = reading_date
            self.present_reading = present_reading
            self.previous_reading = previous_reading
            self.consumption_cubic_meter = consumption_cubic_meter

        def display_metering_information(self):
            # display the information provided
            print("                   METERING INFORMATION                    ")
            print("Meter No.:         MRU No.:            Seq No.:       ")
            print(self.meter_no, " ", self.mru_no, " ",   self.seq_no, " ")
            print("Reading Date      : ", self.reading_date)
            print("Present Reading   : ", self.present_reading)
            print("Previous Reading  : ", self.previous_reading)
            print("Consumption (cu.m): ", self.consumption_cubic_meter)
            print("                                                           ")
            print("Previous 3 Months Consumption")
            print("-----------------------------------------------------------")
            print("                   BILL & PAYMENT HISTORY                  ")
            print("Desc       Total Amount          OR#         Date          ")
            print("                                                           ")
            print("Description: WB-Water Bill, GD-Guarantee Deposit, MISC-")
            print("Reopening Fee, Connection Fee, Metering Charge")
            print("-----------------------------------------------------------")

class Billing_Summary_information:
        def __init__(self):
            # billing summary data initialization
            self.billing_period = ""
            self.current_charges = 0.00
            self.basic_charge = 0.00
            self.environmental_charges = 0.00
            self.msc = 0.00
            self.total_current_charges_before_taxes = 0.00
            self.government_taxes = 0.00
            self.consumption_cubic_meter = 0.00
            self.total_amount_due = 0.00
            self.payment_due_date = ""

        def ccm(self, consumption_cubic_meter, payment_due_date, msc):
            # compute the following charges
            self.consumption_cubic_meter = consumption_cubic_meter
            self.msc = msc
            self.basic_charge = 23.52 * consumption_cubic_meter
            self.environmental_charges = (self.basic_charge * 0.20)
            self.total_current_charges_before_taxes = self.basic_charge + self.environmental_charges + self.msc
            self.government_taxes = ((self.basic_charge * self.environmental_charges * self.msc) * 0.025)

            #compute for total amount due
            self.total_amount_due = self.total_current_charges_before_taxes + self.government_taxes

            #input payment due date
            self.payment_due_date = payment_due_date

        def display_billing_summary(self):
            # display the billing summary
            print("                      BILLING SUMMARY                      ")
            print("BILLING PERIOD: ", self.billing_period)
            print("Current Charges                                  ", self.current_charges)
            print(f"Basic Charge                                    ", self.basic_charge)
            print(f"Environmental Charges (20% of basic charge)     ", self.environmental_charges)
            print(f"Maintenance Service Charge (MSC)                ", self.msc)
            print(f"Total Current Charges Before Taxes              ", self.total_current_charges_before_taxes)
            print(f"Government Taxes                                ", self.government_taxes)
            print("")
            print("")
            print("-----------------------------------------------------------")
            print("TOTAL AMOUNT DUE:                                ", self.total_amount_due)
            print("PAYMENT DUE DATE:                                ", self.payment_due_date)