
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if not self.grades:
            return 0
        total_grades = sum(self.grades.values())
        num_subjects = len(self.grades)
        return total_grades / num_subjects

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        print(f"Average Grade: {average:.2f}")
        print(f"Overall Letter Grade: {letter_grade}")


class School:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")

    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            print(f"No student found with ID {student_id}.")
        else:
            self.students[student_id].add_grade(subject, grade)
            print(f"Grade {grade} added for {subject}.")

    def display_student(self, student_id):
        if student_id not in self.students:
            print(f"No student found with ID {student_id}.")
        else:
            self.students[student_id].display_info()

    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                student.display_info()
                print("-" * 30)


# Example usage
if __name__ == "__main__":
    school = School()

    # Adding students
    school.add_student(1, "Alice")
    school.add_student(2, "Bob")

    # Adding grades
    school.add_grade(1, "Math", 85)
    school.add_grade(1, "Science", 90)
    school.add_grade(2, "Math", 78)
    school.add_grade(2, "Science", 88)

    # Display individual student
    school.display_student(1)

    # Display all students
    school.display_all_students()
