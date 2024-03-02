# Define functions
def student_info():
    name = input("Enter student's name: ")
    id = input("Enter student's ID: ")
    dob = input("Enter student's DOB (DD/MM/YYYY): ")
    return {'Name': name, 'ID': id, 'DOB': dob}

def course_info():
    cname = input("Enter course's name: ")
    cid = int(input("Enter course's ID: "))
    return {'Course name': cname, 'Course ID': cid}

def list_students(student_list):
    print("List of students:")
    for student in student_list:
        print(student)

def list_courses(course_list):
    print("List of courses:")
    for course in course_list:
        print(course)

def marking(student_list, course_list):
    # Display the list of courses to choose from
    list_courses(course_list)
    chosen_course = int(input("Choose a course (Enter the course ID): "))

    # Find the selected course
    selected = None
    for course in course_list:
        if course['Course ID'] == chosen_course:
            selected = course
            break

    # Check if the course ID is valid
    if selected is None:
        print("Invalid ID")
        return

    # Input marks for the selected course for each student
    print(f"Enter marks for the course: {selected['Course name']}")
    for student in student_list:
        mark = float(input(f"Enter mark for {student['Name']} in {selected['Course name']}: "))
        if 'Courses' not in student:
            student['Courses'] = {}
        student['Courses'].setdefault(selected['Course name'], {})['Marks'] = mark

def show_mark(student_list, course_list):
    # Display the list of courses to choose from
    list_courses(course_list)
    chosen_course = int(input("Choose a course (Enter the course ID): "))

    # Find the selected course
    selected = None
    for course in course_list:
        if course['Course ID'] == chosen_course:
            selected = course
            break

    # Check if the course ID is valid
    if selected is None:
        print("Invalid ID")
        return

    # Display marks for the selected course for each student
    print(f"Showing marks for the course: {selected['Course name']}")
    for student in student_list:
        if 'Courses' in student and selected['Course name'] in student['Courses']:
            marks = student['Courses'][selected['Course name']].get('Marks', 'Marks not available')
            print(f"Student: {student['Name']} - Marks: {marks}")

# Main
numberOfStudents = int(input("Enter number of students: "))
studentARR = []
for i in range(numberOfStudents):
    studentARR.append(student_info())

numberOfCourses = int(input("Enter number of courses: "))
courseARR = []
for i in range(numberOfCourses):
    courseARR.append(course_info())

marking(studentARR, courseARR)
show_mark(studentARR, courseARR)
    