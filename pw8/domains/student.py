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
