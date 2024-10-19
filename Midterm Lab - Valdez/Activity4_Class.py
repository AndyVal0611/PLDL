# this program will have a student assessment form through attributes and classes
class Student:
    def __init__(self):
        self.student_name = ""
        self.course = ""
        self.student_number = ""
        self.academic_year = ""

    def get_student_info_data(self, name, student_number, course, academic_year):
        self.student_name = name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year

    def display_student_information(self):
        print("student name: ", self.student_name)
        print("course: ", self.course)
        print("student number: ", self.student_number)
        print("academic year: ", self.academic_year)

class Subject_info:
    def __init__(self):
        self.section1 = 0.00
        self.subject1 = 0.00
        self.unit1 = 0.00
        self.section2 = 0.00
        self.subject2 = 0.00
        self.unit2 = 0.00
        self.section3 = 0.00
        self.subject3 = 0.00
        self.unit3 = 0.00
        self.section4 = 0.00
        self.subject4 = 0.00
        self.unit4 = 0.00
        self.section5 = 0.00
        self.subject5 = 0.00
        self.unit5 = 0.00

class assessment_of_fees:
    def get_assessment_fees(self):
        self.adu_chronicle = input("AdU Chronicle: ")
        self.athletic = input("Athletic: ")
        self.audio_visual = input("Audio-visual :")
        self.ausg = input("AUSG: ")
        self.cultural_fee = int(input("Cultural Fee: ")
        self.enegycost_airconclass = int(input("Energy Cost/Aircon Class: "_)
        self.guidance = input("Guidance: ")
        self.insurance_fee = int(input("Insurance Fee: ")
        self.learning_management_system = int(input("Learning Management System: ")
        self.library_fee = int(input("Library fee: ")
        self.medical_and_dental = input("Medical and Dental: ")
        self.registration = input("Self-registration: ")
        self.rso =
        self.student_activities_fee =
        self.student_nurturance_fee =
        self.technology_fee =
        self.test_papers =
        self.assessment_amt =
        self.downpayment =