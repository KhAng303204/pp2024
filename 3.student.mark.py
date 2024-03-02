import math
import numpy as np
import curses

class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.courses = {}

    def add_mark(self, course_name, mark):
        self.courses[course_name] = round(mark, 1)

    def calculate_gpa(self):
        total_credits = 0
        weighted_sum = 0
        for course_name, mark in self.courses.items():
            course_credits = 3
            weighted_sum += course_credits * mark
            total_credits += course_credits
        return weighted_sum / total_credits

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

    def calculate_gpa_for_all_students(self):
        gpa_list = []
        for student in self.students:
            gpa = student.calculate_gpa()
            gpa_list.append(gpa)
        return gpa_list

    def sort_students_by_gpa(self):
        gpa_list = self.calculate_gpa_for_all_students()
        sorted_students = [student for _, student in sorted(zip(gpa_list, self.students), reverse=True)]
        return sorted_students

    def display_gpa_table(self):
        sorted_students = self.sort_students_by_gpa()
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            while True:
                stdscr.clear()
                stdscr.addstr(0, 0, "GPA Table")
                stdscr.addstr(2, 0, "Rank\tName\t\tGPA")
                for i, student in enumerate(sorted_students):
                    stdscr.addstr(3 + i, 0, f"{i + 1}\t{student.name.ljust(20)}\t{student.calculate_gpa():.2f}")

                stdscr.addstr(len(sorted_students) + 4, 0, "Press q to quit...")
                stdscr.refresh()

                c = stdscr.getch()
                if c == ord('q'):
                    break
        finally:
            curses.echo()
            curses.nocbreak()
            stdscr.keypad(False)
            curses.endwin()

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
    school.display_gpa_table()

if __name__ == "__main__":
    main()
