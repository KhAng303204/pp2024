import gzip
import pickle
import shutil
import threading
from input import write_to_file, check_file_exist

# Existing code...

def main():
    # Check if students.dat exists
    if check_file_exist('students.dat'):
        decompress_and_load_data('students.dat')

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

    # Start a background thread to save data using pickle and compression
    persistence_thread = threading.Thread(target=save_data, args=('students.pickle', 'courses.pickle', 'marks.pickle'))
    persistence_thread.start()

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

# Rest of the code remains the same...
