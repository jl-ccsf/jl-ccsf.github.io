'''
d7_student_data.py
jl-ccsf
07/17/2026
CS-131B, Prof. Ibrahim
Populates rows in data table using an object class for each student.
'''

class Student:

    '''Initializes object class'''
    def __init__ (self, name, id, dept, prog):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__prog = prog
    
    '''Definess class mutators'''
    def set_name (self, name):
        self.__name = name
    def set_id (self, id):
        self.__id = id
    def set_dept (self, dept):
        self.__dept = dept
    def set_prog (self, prog):
        self.__prog = prog
    
    '''Defines class accessors'''
    def get_name (self):
        return self.__name
    def get_id (self):
        return self.__id
    def get_dept (self):
        return self.__dept
    def get_prog (self):
        return self.__prog

def main():

    # Constructs student data from class
    student_1 = Student("Marie Curie", 189300, "Physical Science", "Bachelor's in Physics")
    student_2 = Student("Terry Pratchett", 200900, "Humanities", "Honorary Doctorate of Literature")
    student_3 = Student("Guido van Rossum", 198200, "Computer Science", "Master's in Computer Science")

    # Stores student data in list
    students = [student_1, student_2, student_3]

    # Formats and displays data for each student
    for i in range (len(students)):
        print(f"Name: {students[i].get_name()}")
        print(f"ID: {students[i].get_id()}")
        print(f"Dept: {students[i].get_dept()}")
        print(f"Program: {students[i].get_prog()}")
        print()

# Initializes program
if __name__ == "__main__":
    main()

'''
SAMPLE RUN

Name: Marie Curie
ID: 189300
Dept: Physical Science
Program: Bachelor's in Physics

Name: Terry Pratchett
ID: 200900
Dept: Humanities
Program: Honorary Doctorate of Literature

Name: Guido van Rossum
ID: 198200
Dept: Computer Science
Program: Master's in Computer Science
'''