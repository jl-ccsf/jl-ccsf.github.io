'''
p6_course.py
jl-ccsf
07/14/2026
CS-131B, Prof. Ibrahim
Collects key-value pairs for course names, rooms, instructors, and locations. 
Concatenates and displays class info based on user input.
'''

# Defines constants
START = "Enter course number: "
ERROR = "ERROR: Course not found."
RETRY = "Please re-enter course number: "
RESTART = "Choose another course? [y/n]: "

# Defines dictionaries
classrooms = {"CS101" : 3004, "CS102" : 4501, "CS103" : 6755, "NT110" : 
              1244, "CM241" : 1411}
instructors = {"CS101" : "Haynes", "CS102" : "Alvarado", "CS103" : "Rich", 
               "NT110" : "Burke", "CM241" : "Lee"}
class_times = {"CS101" : "8:00 a.m.", "CS102" : "9:00 a.m.", "CS103" : 
               "10:00 a.m.", "NT110" : "11:00 a.m.", "CM241" : "1:00 p.m."}

def main():

    # Assigns course value
    course = input(START)

    # Fails initial loop
    if valid_course(course) == False:
        course = retry(course)
        valid_course(course)

    # Passes initial loop
    while valid_course(course) == True:
        # Displays course schedule
        print(get_sched(course))
        print() # Blank line

        # Checks for initial value
        if restart() == True:
            print() # Blank line
            # Re-initializes
            course = input(START)
            while valid_course(course) == False:
                course = retry(course)
                valid_course(course)
        # Checks for terminal value
        else:
            # Terminates
            break

'''Validates course input'''
def valid_course(key):
    # Checks for key
    if key in classrooms:
        # Confirms valid
        valid = True
    else:
        # Confirms invalid
        valid = False
    # Saves Boolean
    return valid

'''Assigns variables and formats output'''
def get_sched(key):
    room = classrooms[key]
    prof = instructors[key]
    time = class_times[key]
    course_sched = f"{key} is in Room {room} with Prof. {prof} at {time}"
    return course_sched

'''Validates restart input'''
def restart():

    # Prompts for restart
    another = input(RESTART).lower()

    # Checks for initializor
    if another == "y":
        # Confirms initialization
        restart = True
    # Checks for terminator
    else:
        # Confirms termination
        restart = False
    # Saves Boolean
    return restart

'''Sets retry error messages'''
def retry(key):

    # Reports error
    print(ERROR)

    # Prompts re-entry
    key = input(RETRY)

    # Saves input value
    return key

main()

'''
SAMPLE RUN A: ALL VALID

Enter course number: CS101
CS101 is in Room 3004 with Prof. Haynes at 8:00 a.m.

Choose another course? [y/n]: y

Enter course number: CS102
CS102 is in Room 4501 with Prof. Alvarado at 9:00 a.m.

Choose another course? [y/n]: y

Enter course number: CS103
CS103 is in Room 6755 with Prof. Rich at 10:00 a.m.

Choose another course? [y/n]: y

Enter course number: NT110
NT110 is in Room 1244 with Prof. Burke at 11:00 a.m.

Choose another course? [y/n]: y

Enter course number: CM241
CM241 is in Room 1411 with Prof. Lee at 1:00 p.m.

Choose another course? [y/n]: n

SAMPLE RUN B: ALL INVALID

Enter course number: CS201
ERROR: Course not found.
Please re-enter course number: CS101
CS101 is in Room 3004 with Prof. Haynes at 8:00 a.m.

Choose another course? [y/n]: y

Enter course number: CS202
ERROR: Course not found.
Please re-enter course number: CS102
CS102 is in Room 4501 with Prof. Alvarado at 9:00 a.m.

Choose another course? [y/n]: y

Enter course number: CS203
ERROR: Course not found.
Please re-enter course number: CS103
CS103 is in Room 6755 with Prof. Rich at 10:00 a.m.

Choose another course? [y/n]: y

Enter course number: NT210
ERROR: Course not found.
Please re-enter course number: NT110
NT110 is in Room 1244 with Prof. Burke at 11:00 a.m.

Choose another course? [y/n]: y

Enter course number: CM221
ERROR: Course not found.
Please re-enter course number: CM241
CM241 is in Room 1411 with Prof. Lee at 1:00 p.m.

Choose another course? [y/n]: n
'''
