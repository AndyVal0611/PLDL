import Activity4_Class

class Student_Info_Input:
    def get_student_input(self):
        obj = Activity4_Class.Student_Info()
        obj2 = Activity4_Class.Assessment_Amount()
        print("- STUDENT INFORMATION -")
        name = input("Student name: ")
        course = input("Student course: ")
        number = input("Student number: ")
        academic_year = input("Academic year: ")
        printed_date = input("Date printed: ")

class Course_Outline_Input:
    def get_course_outline(self):
        total_subjects = int(input("Total number of subjects: "))
        subjects = []

        for i in range(total_subjects):
            subject = input(f"Enter Subject {i + 1}: ")
            units = int(input(f"Enter No. of Unit {i + 1}: "))
            section = input(f"Enter Section for the Subject {i + 1}: ")
            course_outline = Activity4_Class.Student_Info()
            course_outline.get_course_outline(total_subjects, section, units, subject)
            subjects.append(course_outline)

        student_data = obj.get_student_data(name, course, number, academic_year, printed_date)
        obj.display_student_data()
        obj.total_units_calculation(subjects)
        obj.display_student_outline(subjects)


student_info = Student_Info_Input()
student_info.get_student_input()