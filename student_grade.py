class StudentGradeManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, student_name):
        if student_id not in self.students:
            self.students[student_id] = {"name": student_name, "grades": {}}
            print(f"Student {student_name} added successfully.")
        else:
            print("Student ID already exists.")

    def add_grade(self, student_id, course, grade):
        if student_id in self.students:
            self.students[student_id]["grades"][course] = grade
            print(f"Grade added for {self.students[student_id]['name']} in {course}.")
        else:
            print("Student ID not found.")

    def get_grades(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Grades for {student['name']}:")
            for course, grade in student["grades"].items():
                print(f"{course}: {grade}")
        else:
            print("Student ID not found.")

    def get_student_average(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id]["grades"].values()
            if grades:
                average = sum(grades) / len(grades)
                print(f"Average grade for {self.students[student_id]['name']}: {average:.2f}")
            else:
                print("No grades available for the student.")
        else:
            print("Student ID not found.")

def main():
    system = StudentGradeManagementSystem()

    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Grades")
        print("4. Get Student Average")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            system.add_student(student_id, student_name)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            course = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            system.add_grade(student_id, course, grade)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            system.get_grades(student_id)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            system.get_student_average(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
