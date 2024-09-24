'''
Create a students report card class showing following detials as table
- name
- roll no.
- Maths marks
- physics marks
- chemistry marks
- eng marks
- total percentage 

Note: should not consider the class of the student in which
they are studying but the table will be showing the a group of students of one class. 

You can add more methods such as ID function that shows the ID card of a Student A with 
RollNo. , Blood group, Address and Parents name, emailID.


'''
from prettytable import PrettyTable
"""PrettyTable is a simple Python class library that alows user to easily display 
   tabular data in a visually appealing ASCII table format.
   Documentation link -----> https://pypi.org/project/prettytable/"""

class Student:
    """The Student class contains multiple attributes related to student details.
       It also contains a method called add_student() which adds student details and returns the student roll number."""
    def __init__(self):
        self.name = None
        self.roll_number = None
        self.m_marks = None
        self.p_marks = None
        self.c_marks = None
        self.eng_marks = None
        self.percent = None
        self.b_group = None
        self.address = None
        self.m_name = None
        self.f_name = None
        self.email = None

    def add_student(self):
        self.name = input("\nEnter the student's name: ")
        self.roll_number = input("Enter the student's roll no: ")
        self.m_marks = int(input("Enter the student's maths marks: "))
        self.p_marks = int(input("Enter the student's physics marks: "))
        self.c_marks = int(input("Enter the student's chemistry marks: "))
        self.eng_marks = int(input("Enter the student's english marks: "))
        self.percent = round(((self.m_marks + self.p_marks + self.c_marks + self.eng_marks)/5), 2)
        self.b_group = input("Enter the student's blood group: ")
        self.address = input("Enter the student's address: ")
        self.m_name = input("Enter the student's mother's name: ")
        self.f_name = input("Enter the student's father's name: ")
        self.email = input("Enter the student's email: ")
        return self.roll_number


def classroom():
    number_of_students = 0
    class_details = {}
    while True:
        options = ["Type '+' to add a student's info.","Type 'report' to view a student's report.","Type 'ID' to view a student's id.","Type 'exit' to exit class."]
        user_choice = input(f"\nWhat do you want to do?\n1.{options[0]}\n2.{options[1]}\n3.{options[2]}\n4.{options[3]}\n").lower()

        if user_choice == "+":
            student = Student()
            roll_no = student.add_student()
            class_details[roll_no] = student
            number_of_students += 1
        elif user_choice == "report":
            if number_of_students == 0:
                print("No student reports found in this classroom.")
            else:
                student_roll_no = input("Enter the roll no. of the student: ")
                for head_count in class_details:
                    if head_count == student_roll_no:
                        concerned_student = class_details[head_count]
                        report_table = PrettyTable(["Name","Roll no.","Maths","Physics","Chemistry","English","Total Percentage"])
                        report_table.add_row([concerned_student.name,concerned_student.roll_number,concerned_student.m_marks,concerned_student.p_marks,concerned_student.c_marks,concerned_student.eng_marks,concerned_student.percent])
                        print(report_table)
                    else:
                        print("No student data found,please enter a valid roll number.")
        elif user_choice == "id":
            if number_of_students == 0:
                print("No student IDs found in this classroom.")
            else:
                student_roll_no = input("Enter the roll no. of the student: ")
                for head_count in class_details:
                    if head_count == student_roll_no:
                        concerned_student = class_details[head_count]
                        id_table = PrettyTable(["Blood Group","Address","Mother's Name","Father's Name","E-mail"])
                        id_table.add_row([concerned_student.b_group,concerned_student.address,concerned_student.m_name,concerned_student.f_name,concerned_student.email])
                        print(id_table)
                    else:
                        print("No student data found,please enter a valid ID.")
        elif user_choice == "exit":
            exit()

if __name__ == '__main__':
    classroom()