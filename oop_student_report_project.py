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
import time
"""time is a python module which allows user to work with time by providing functionalities like getting the current time,
 pausing the Program from executing, etc. """

from prettytable import PrettyTable
"""PrettyTable is a simple Python class library that alows user to easily display 
   tabular data in a visually appealing ASCII table format.
   Documentation link -----> https://pypi.org/project/prettytable/"""

class Student:
     """
    Represents a student with various attributes such as name, roll number, marks in different subjects,
    percentage, blood group, address, and parent information.

    Attributes:
        name (str): The student's full name.
        roll_number (str): The student's roll number.
        m_marks (int): Marks obtained in mathematics.
        p_marks (int): Marks obtained in physics.
        c_marks (int): Marks obtained in chemistry.
        eng_marks (int): Marks obtained in English.
        percent (float): Overall percentage calculated as the average of subject marks.
        b_group (str): Blood group of the student.
        address (str): Address of the student.
        m_name (str): Mother's name.
        f_name (str): Father's name.
        email (str): Email address of the student.

    Methods:
        add_student(): Allows user input to set the attributes for a student instance.
    """
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
        """
        Prompts the user to input details for a student and calculates the overall percentage.
        """

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

def add_info(class_info, student_count):
    """
    Add student information to the class details.

    Args:
    class_details (dict): Dictionary containing student information.
    num_students (int): Current number of students.

    Returns: (tuple: Updated class_details and num_students.)
    """
    student = Student()
    student.add_student()
    class_info[student.roll_number] = student
    student_count += 1
    return class_info,student_count

def generate_report(total_students, class_data):
    """
    Generate a report based on student information.

    Args:
    num_students (int): Current number of students.
    class_details (dict): Dictionary containing student information.

    Returns: None
    """
    if  total_students == 0:
        print("No student reports found in this classroom.")
    else:
        student_roll_no = input("Enter the roll no. of the student: ")
        if student_roll_no in class_data:
            concerned_student = class_data[student_roll_no]
            report_table = PrettyTable(["Name","Roll no.","Maths","Physics","Chemistry","English","Total Percentage"])
            report_table.add_row([concerned_student.name,concerned_student.roll_number,concerned_student.m_marks,concerned_student.p_marks,concerned_student.c_marks,concerned_student.eng_marks,concerned_student.percent])
            print(report_table)
        else:
            print("No student data found,please enter a valid roll number.")

def generate_identity(total_students, class_data):
    """
    Generate a student's ID.
    
    Args:
    num_students (int): Current number of students.
    class_details (dict): Dictionary containing student information.
    
    Returns: None
    """
    if  total_students == 0:
        print("No student IDs found in this classroom.")
    else:
        student_roll_no = input("Enter the roll no. of the student: ")
        if student_roll_no in class_data:
            concerned_student = class_data[student_roll_no]
            id_table = PrettyTable(["Blood Group","Address","Mother's Name","Father's Name","E-mail"])
            id_table.add_row([concerned_student.b_group,concerned_student.address,concerned_student.m_name,concerned_student.f_name,concerned_student.email])
            print(id_table)
        else:
            print("No student data found,please enter a valid ID.")

def exit_class():
    """
    Exit the classroom.
    Returns: None
    """
    time.sleep(2)
    print("You have exited the classroom.")
    exit()
    
def classroom():
    """
    Manage a classroom by allowing user interactions to add student info,
    generate reports, and view student IDs.

    Usage:
    (Adding a student's info, Viewing a student's report, Viewing a student's ID, Exiting class)

    Returns: None
    """
    number_of_students = 0
    class_details = {}
    while True:
        options = ["Type '+' to add a student's info.","Type 'report' to view a student's report.","Type 'ID' to view a student's id.","Type 'exit' to exit class."]
        user_choice = input(f"\nWhat do you want to do?\n1.{options[0]}\n2.{options[1]}\n3.{options[2]}\n4.{options[3]}\n").lower()

        if user_choice == "+":
            class_details,number_of_students = add_info(class_details, number_of_students)

        elif user_choice == "report":
            generate_report(number_of_students,class_details)

        elif user_choice == "id":
            generate_identity(number_of_students,class_details)
        elif user_choice == "exit":
            exit_class()

if __name__ == '__main__':
    classroom() 