#define function
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

#marking
def marking(student_list, course_list):
    list_courses(course_list)
    chosen_course = int(input("Choose a course (Enter the course ID)"))

    #find the chosen  course
    selected = None
    for course in course_list:
        if course['course ID'] == chosen_course:
            selected = course
            break
    if selected is None:
        print("Invalid ID")
        return

    print(f"Enter mark for the course: {selected['Course name']}")

    #input mark
    for student in student_list:
        mark = float(input(f"Enter mark for {student['Name']} in {selected['Course name']}")) 
        student.setdefault('Courses', {}).setdefault(selected['Course name'], {})['Marks'] = mark
        #setdefault('Courses', {}): check if the course exits in dics
        #setdefault(selected['Course name'], {}): match the name of course
        #['Marks'] = mark: marking the course

def show_mark(student_list, course_list):
    list_courses(course_list)
    chosen_course = int(input("Choose a course (Enter the course ID)"))

    #find the chosen  course
    selected = None
    for course in course_list:
        if course['course ID'] == chosen_course:
            selected = course
            break
    if selected is None:
        print("Invalid ID")
        return

    print(f"Showing marks for the course: {selected['Course name']}")

    #Display the marks
    for student in student_list:
        if 'Courses' in student and selected['Course name'] in student['Courses']:
             marks = student['Courses'][selected['Course name']].get('Marks', 'Marks not available')
             print(f"Student: {student['Name']} - Marks: {marks}")

#main
numberOfStudents = int(input("Enter number of students: "))
studentARR = [] #empty list 2 store students i4
for i in range(numberOfStudents):        #the loop run number of student times 2 create dics
    studentARR.append(student_info())

numberOfCourses = int(input("Enter number of courses: "))
courseARR = [] #empty list 2 store courses i4
for i in range(numberOfCourses):         #the loop run number of course times 2 create dics
    courseARR.append(course_info())

list_students(studentARR)
list_courses(courseARR)










