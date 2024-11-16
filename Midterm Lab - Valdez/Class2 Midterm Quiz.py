



    def display_personal_info(self):
        print("Customer Name:", self.customer_name)
        print("Address:", self.address)
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