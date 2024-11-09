class Student_Info:
    tuition_fee_lecture = 1551.00

    def __init__(self):
        self.student_name = ""
        self.student_course = ""
        self.student_number = ""
        self.academic_year = ""
        self.printed_date = ""
        self.student_section = ""
        self.student_subject = ""
        self.student_total_subjects = 0.00
        self.student_units = 0.00
        self.total_units = 0.00
        self.tuition_fee_lecture = 1551.00
        self.unit_tuition_fee = 0.00

    def total_units_calculation(self, subjects):
        for i, course_outline in enumerate(subjects, start = 1):
            self.total_units += int(sum({course_outline.student_units}))
        return self.total_units

    def display_student_data(self):
        width = 85
        name_width = 38
        number_width = 18
        course_width = 38
        year_width = 18

        print("\t\t\t\t              CERTIFICATE OF ENROLMENT              \t\t\t\t")
        print("\t\t\t\t            1st Semester, A.Y. 2024-2025              \t\t\t\t")
        print(f"NAME   : {self.student_name:<{name_width}}\t\t  STUDENT NO. : {self.student_number:<{number_width}}\t ")
        print(f"COURSE : {self.student_course:<{course_width}}\t  ACAD. YEAR  : {self.academic_year:<{year_width}}\t ")
        print("-" * width)

    def display_student_outline(self, subjects):
        width = 85
        subject_width = 33
        section_width = 11
        date_width = 23
        print("\t  SECTION   \t\t\t\t      SUBJECT      \t\t\t\t        UNITS  \t")
        print("-" * width)
        for i, course_outline in enumerate(subjects, start = 1):
          print(f"\t  {course_outline.student_section:<{section_width}} \t  {course_outline.student_subject:<{subject_width}}\t\t\t\t\t\t  {course_outline.student_units}\t\t |")
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal Units: {self.total_units:.0f} \t\t ")
        print("-" * width)
        print(f"DATE PRINTED \t: {self.printed_date:<{date_width}} \t\t\t\t\t\t\t\t   ")
        print("-" * width)

class Assessment_Amount:
    tuition_fee_lecture = 1551.00

    def __init__(self):
        self.tuition_fee_lecture = 1551.00
        self.total_units = 0.00
        self.tuition_fee_lecture_total = 0.00
        self.adu_chronical = 0.00
        self.athletic = 0.00
        self.audio_visual_library = 0.00
        self.ausg = 0.00
        self.cultural_fee = 0.00
        self.energy_cost = 0.00
        self.guidance = 0.00
        self.insurance_fee = 0.00
        self.learning_management_system = 0.00
        self.library_fee = 0.00
        self.medical_dental = 0.00
        self.registration = 0.00
        self.rso = 0.00
        self.student_activities = 0.00
        self.student_nurturance = 0.00
        self.technology_fee = 0.00
        self.test_papers = 0.00
        self.other_assessment = 0.00
        self.downpayment = 0.00
        self.total_due = 0.00
        self.prelim = 0.00
        self.midterm = 0.00
        self.final = 0.00

    def get_tuition_fee_lecture(self, total_units):
        self.tuition_fee_lecture_total = total_units * 1551.00
        return self.tuition_fee_lecture_total

    def get_student_assesssment(self, adu_chronical, athletic, audio_visual_library, ausg, cultural_fee, energy_cost, guidance,
    insurance_fee, learning_management_system, library_fee, medical_dental, registration, rso, student_activities, student_nurturance,
    technology_fee, test_papers, downpayment):
        self.adu_chronical = adu_chronical
        self.athletic = athletic
        self.audio_visual_library = audio_visual_library
        self.ausg = ausg
        self.cultural_fee = cultural_fee
        self.energy_cost = energy_cost
        self.guidance = guidance
        self.insurance_fee = insurance_fee
        self.learning_management_system = learning_management_system
        self.library_fee = library_fee
        self.medical_dental = medical_dental
        self.registration = registration
        self.rso = rso
        self.student_activities = student_activities
        self.student_nurturance = student_nurturance
        self.technology_fee = technology_fee
        self.test_papers = test_papers

        self.other_assessment = (self.tuition_fee_lecture_total + adu_chronical + athletic + audio_visual_library + ausg +
        cultural_fee + energy_cost + guidance + insurance_fee + learning_management_system + library_fee + medical_dental
        + registration + rso + student_activities + student_nurturance + technology_fee + test_papers)

        self.downpayment = downpayment
        self.total_due = self.other_assessment - downpayment

        term_amount = round((self.other_assessment - downpayment) / 3, 2)
        remainder = round((self.other_assessment - downpayment) - (term_amount * 3), 2)

        self.prelim = term_amount
        self.midterm = term_amount
        self.final = term_amount + remainder

        return self.other_assessment, self.total_due, self.prelim, self.midterm, self.final

    def display_assessment(self):
        line_length = 50
        width = 15
        print("-" * 51)
        print("\t\t       ASSESSMENT OF FEES\t\t       ")
        print("-" * 51)
        print(f"TUITION FEE LECTURE \t\t\t {self.tuition_fee_lecture:<{width}.2f} \t")
        print(f"AdU CHRONICAL \t\t\t\t {self.adu_chronical:<{width}.2f} \t")
        print(f"ATHLETIC     \t\t\t\t\t {self.athletic:<{width}.2f} \t")
        print(f"AUDIO-VISUAL LIBRARY \t\t\t {self.audio_visual_library:<{width}.2f} \t")
        print(f"AUSG     \t\t\t\t\t\t {self.ausg:<{width}.2f} \t")
        print(f"CULTURAL FEE \t\t\t\t\t {self.cultural_fee:<{width}.2f} \t")
        print(f"ENERGY COST, AIRCON CLASSROOM \t\t {self.energy_cost:<{width}.2f} \t")
        print(f"GUIDANCE     \t\t\t\t\t {self.guidance:<{width}.2f} \t")
        print(f"INSURANCE FEE \t\t\t\t {self.insurance_fee:<{width}.2f} \t")
        print(f"LEARNING MANAGEMENT SYSTEM \t {self.learning_management_system:<{width}.2f} \t")
        print(f"LIBRARY FEE \t\t\t\t\t {self.library_fee:<{width}.2f} \t")
        print(f"MEDICAL AND DENTAL \t\t\t {self.medical_dental:<{width}.2f} \t")
        print(f"REGISTRATION \t\t\t\t\t {self.registration:<{width}.2f} \t")
        print(f"RSO \t\t\t\t\t\t\t\t\t\t {self.rso:<{width}.2f} \t")
        print(f"STUDENT ACTIVITIES FEE \t\t {self.student_activities:<{width}.2f} \t")
        print(f"STUDENT NURTURANCE FEE \t\t {self.student_nurturance:<{width}.2f} \t")
        print(f"TECHNOLOGY FEE \t\t\t\t {self.technology_fee:<{width}.2f} \t")
        print(f"TEST PAPERS     \t\t\t\t {self.test_papers:<{width}.2f} \t")
        print(f"Assessment Amount \t\t\t: {self.other_assessment:<{width}.2f} \t")
        print(f"Downpayment \t\t\t\t\t: {self.downpayment:<{width}.2f} \t")
        print(" " * 51)
        print("-" * 51)
        print(f"| Total Due \t\t\t\t\t: {self.total_due:<{width}.2f} ")
        print("-" * 51)
        print("\t\t       Schedule Of Payment\t\t       ")
        print("-" * 51)
        print(f"PRELIM     \t\t\t\t\t {self.prelim:<{width}.2f}")
        print(f"MIDTERM     \t\t\t\t\t {self.midterm:<{width}.2f}")
        print(f"FINAL     \t\t\t\t\t {self.final:<{width}.2f}")
        print("-" * 51)