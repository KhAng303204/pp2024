from domains.student import Student
from domains.course import Course
from input import get_float_input, get_int_input
from output import display_gpa_table

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    # Implement the rest of the SchoolSystem class methods here...

def main():
    school = SchoolSystem()

    # Adding students
    student1 = Student("John Doe", 1, "2000-01-01")
    student2 = Student("Jane Smith", 2, "2001-02-02")
    school.add_student(student1)
    school.add_student(student2)

    # Adding courses
    course1 = Course("Math", 101)
    course2 = Course("Physics", 102)
    school.add_course(course1)
    school.add_course(course2)

    # Marking
    school.marking()

    # Display GPA Table
    sorted_students = school.sort_students_by_gpa()
    display_gpa_table(sorted_students)

if __name__ == "__main__":
    main()
