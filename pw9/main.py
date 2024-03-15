import gzip
import pickle
import shutil
import threading
import tkinter as tk
from tkinter import messagebox

# Import other modules and classes
from input import get_float_input, get_int_input, write_to_file, check_file_exist
from output import display_gpa_table
from domains.student import Student
from domains.course import Course
from school_system import SchoolSystem

def save_data(*filenames):
    # Serialize and compress data using pickle and gzip
    with gzip.open('students.dat', 'wb') as f_out:
        for filename in filenames:
            with open(filename, 'rb') as f_in:
                shutil.copyfileobj(f_in, f_out)

def decompress_and_load_data(filename):
    with gzip.open(filename, 'rb') as f_in:
        with open('students.pickle', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    with open('students.pickle', 'rb') as file:
        students = pickle.load(file)
        for student in students:
            school.add_student(student)

def on_marking():
    mark_window = tk.Toplevel(root)
    course_var = tk.StringVar()
    mark_var = tk.DoubleVar()

    # Create labels and entry fields for course and mark
    tk.Label(mark_window, text="Choose Course:").pack()
    course_entry = tk.Entry(mark_window, textvariable=course_var)
    course_entry.pack()

    tk.Label(mark_window, text="Enter Mark:").pack()
    mark_entry = tk.Entry(mark_window, textvariable=mark_var)
    mark_entry.pack()

    def save_mark():
        course_name = course_var.get()
        mark = mark_var.get()
        if course_name and mark:
            school.mark_student(course_name, mark)
            mark_window.destroy()
        else:
            messagebox.showwarning("Error", "Please enter both course and mark.")

    tk.Button(mark_window, text="Save Mark", command=save_mark).pack()

def on_display_gpa():
    gpa_window = tk.Toplevel(root)
    tk.Label(gpa_window, text="GPA Table").pack()

    gpa_table = tk.Text(gpa_window)
    gpa_table.pack()

    sorted_students = school.sort_students_by_gpa()
    gpa_table.insert(tk.END, "Rank\tName\t\tGPA\n")
    for i, student in enumerate(sorted_students):
        gpa_table.insert(tk.END, f"{i+1}\t{student.name}\t{student.calculate_gpa():.2f}\n")

def on_exit():
    save_data('students.pickle', 'courses.pickle', 'marks.pickle')
    root.quit()

root = tk.Tk()
root.title("School Management System")

# Create an instance of SchoolSystem
school = SchoolSystem()

# Add some default students and courses
student1 = Student("John Doe", 1, "2000-01-01")
student2 = Student("Jane Smith", 2, "2001-02-02")
school.add_student(student1)
school.add_student(student2)

course1 = Course("Math", 101)
course2 = Course("Physics", 102)
school.add_course(course1)
school.add_course(course2)

# Create buttons for actions
mark_button = tk.Button(root, text="Mark Student", command=on_marking)
mark_button.pack()

display_button = tk.Button(root, text="Display GPA Table", command=on_display_gpa)
display_button.pack()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

root.mainloop()
