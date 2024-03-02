class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.courses = {}

    def add_mark(self, course_name, mark):
        self.courses[course_name] = mark


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student.name)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course.name)

    def marking(self):
        self.list_courses()
        chosen_course_id = int(input("Choose a course (Enter the course ID): "))

        selected_course = None
        for course in self.courses:
            if course.course_id == chosen_course_id:
                selected_course = course
                break

        if selected_course is None:
            print("Invalid ID")
            return

        print(f"Enter marks for the course: {selected_course.name}")
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} in {selected_course.name}: "))
            student.add_mark(selected_course.name, mark)

    def show_marks(self):
        self.list_courses()
        chosen_course_id = int(input("Choose a course (Enter the course ID): "))

        selected_course = None
        for course in self.courses:
            if course.course_id == chosen_course_id:
                selected_course = course
                break

        if selected_course is None:
            print("Invalid ID")
            return

        print(f"Showing marks for the course: {selected_course.name}")
        for student in self.students:
            if selected_course.name in student.courses:
                marks = student.courses[selected_course.name]
                print(f"Student: {student.name} - Marks: {marks}")


school = SchoolSystem()

numberOfStudents = int(input("Enter number of students: "))
for _ in range(numberOfStudents):
    name = input("Enter student's name: ")
    student_id = input("Enter student's ID: ")
    dob = input("Enter student's DOB (DD/MM/YYYY): ")
    student = Student(name, student_id, dob)
    school.add_student(student)

numberOfCourses = int(input("Enter number of courses: "))
for _ in range(numberOfCourses):
    cname = input("Enter course's name: ")
    cid = int(input("Enter course's ID: "))
    course = Course(cname, cid)
    school.add_course(course)

school.marking()
school.show_marks()
