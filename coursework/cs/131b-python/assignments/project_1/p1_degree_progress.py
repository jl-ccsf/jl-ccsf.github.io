'''
p1_student_info.py
jl-ccsf
06/12/2026
CS-131B, Prof. Ibrahim
Collects a student's information and calculates how many credits they need to 
graduate from their degree program.
'''

def main():

    # Assigns user input to variables as string values
    student_name = input("Enter student name: ")
    degree_program = input("Enter degree program: ")
    credits_degree = input("Enter credits required for degree: ")
    credits_taken = input("Enter credits completed so far: ")

    # Calculates difference
    credits_left = int(credits_degree) - int(credits_taken)

    # Displays student information
    print() # Blank line
    print("The student's name is " + student_name + ".")
    print("Their degree program is " + degree_program + ".")
    print("The degree requires " + credits_degree + " credits. They have " \
        "completed " + credits_taken + ".")
    print(student_name + " has " + str(credits_left) + " credits left to take.")

main()

'''
SAMPLE RUN

Enter student name: Jules
Enter degree program: Web Application Programming
Enter credits required for degree: 21
Enter credits completed so far: 12

The student's name is Jules.
Their degree program is Web Application Programming.
The degree requires 21 credits. They have completed 12.
Jules has 9 credits left to take.
'''
