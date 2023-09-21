# cgpa 
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
  Creating a list of student objects
students = [
    Student("Alice", "001", 3.8),
    Student("Bob", "002", 3.9),
    Student("Charlie", "003", 3.7),
    Student("David", "004", 4.0),
]

# Sorting the students by CGPA in descending order
sorted_students = sort_students(students)

# Printing the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")