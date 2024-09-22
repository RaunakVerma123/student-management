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

You can add more methods such as ID function that shows the ID card of a Student A with RollNo. , Blood group, Address and Parents name, emailID.


'''
from prettytable import PrettyTable

class Student:
        
    def __init__(self, name, r_num, m_marks, p_marks, c_marks, eng_marks, b_group, address, m_name, f_name, email):
        self.name = name
        self.r_num = r_num
        self.m_marks = m_marks
        self.p_marks = p_marks
        self.c_marks = c_marks
        self.eng_marks = eng_marks
        self.percent = round(((self.m_marks + self.p_marks + self.c_marks + self.eng_marks)/5)*100, 2)
        self.b_group = b_group
        self.address = address
        self.m_name = m_name
        self.f_name = f_name
        self.email = email

def add_student(s_details):
    info = []
    info.append(input("Enter the student's name: "))
    info.append(int(input("Enter the student's roll no: ")))
    info.append(int(input("Enter the student's maths marks: ")))
    info.append(int(input("Enter the student's physics marks: ")))
    info.append(int(input("Enter the student's chemistry marks: ")))
    info.append(int(input("Enter the student's english marks: ")))
    s_details["report"].extend(info)
    info.clear()
    info.append(input("Enter the student's blood group: "))
    info.append(input("Enter the student's address: "))
    info.append(input("Enter the student's mother's name: "))
    info.append(input("Enter the student's father's name: "))
    info.append(input("Enter the student's email: "))
    s_details["id"].extend(info)
    r = s_details["report"]
    id = s_details["id"]
    return r[1], Student(r[0],r[1],r[2],r[3],r[4],r[5],id[0],id[1],id[2],id[3],id[4])


def school():
    student_no = 0
    school_details = {}
    while True:
        options = ["Type '+' to add a student's info.","Type 'report' to view a student's report.","Type 'id' to view a student's id.","Type 'exit' to exit school."]
        
    
        if student_no == 0:
            user_choice = input(f"What do you want to do?\n1.{options[0]}\n2.{options[3]}").lower()
        else:
            user_choice = input(f"What do you want to do next?\n1.{options[0]}\n2.{options[1]}\n3.{options[2]}\n4.{options[3]}").lower()

        if user_choice == '+':
            student_details = {'report':[],'id':[]}
            r_no, tutee = add_student(student_details)
            school_details[r_no] = tutee
            student_no += 1
        elif user_choice == 'report':
            student_roll_no = int(input("Enter the roll no. of the student: "))
            for head_count in school_details:
                if head_count == student_roll_no:
                    report_table = PrettyTable(["Name","Roll no.","Maths","Physics","Chemistry","English"])
                    report_table.add_row([tutee.name,tutee.r_num,tutee.m_marks,tutee.p_marks,tutee.c_marks,tutee.eng_marks])
                    print(report_table)
        elif user_choice == 'id':
            student_roll_no = int(input("Enter the roll no. of the student: "))
            for head_count in school_details:
                if head_count == student_roll_no:
                    id_table = PrettyTable(["Blood Group","Address","Mother's Name","Father's Name","E-mail"])
                    id_table.add_row([tutee.b_group,tutee.address,tutee.m_name,tutee.f_name,tutee.email])
                    print(id_table)
        elif user_choice == 'exit':
            exit()

school()