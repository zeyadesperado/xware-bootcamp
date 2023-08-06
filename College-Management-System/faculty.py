# faculty.py
import os
from professor import FacultyProfessor
from department import Department

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Faculty:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.professors = []
        self.departments = []

    def create_faculty(self):
        print(f"Faculty {self.name} created.")

    def read_faculty_info(self):
        print(f"Faculty Name: {self.name}, Faculty ID: {self.id}")
    
    def update_faculty_info(self, new_name):
        self.name = new_name
        print(f"Updated faculty name: {self.name}")

    def link_professors_to_faculty(self, professor):
        self.professors.append(professor)
        print(f"{professor.name} linked to {self.name} faculty.")

    def link_department_to_faculty(self, department):
        self.departments.append(department)
        print(f"{department.name} linked to {self.name} faculty.")


def main():
    faculty = None
    clear_screen()
    while True:
        print("\nOptions:")
        print("1. Create Faculty ")
        print("2. Read Faculty Info ")
        print("3. Enter Professor Info")
        print("4. Read Professor Info")
        print("5. Update Professor Info")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            clear_screen()
            faculty_id = input("Enter faculty id: ")
            faculty_name = input("Enter faculty name: ")
            faculty = Faculty(faculty_id, faculty_name)
            faculty.create_faculty()
            clear_screen()
            while True:
                name = input("Enter department name (or '-1' to exit): ")
                if name == '-1':
                    break
                id = input("Enter department id: ")
                department = Department(id, name)
                faculty.link_department_to_faculty(department)
                # clear_screen()

        elif choice == "2":
            if faculty:
                faculty.read_faculty_info()
                # input("Press any Button to continue...")
                if faculty.departments:
                    for department in faculty.departments:
                        department.read_specific_department_info()
                        # input("Press any Button to continue...")
                else:
                    print("No departments linked to this faculty yet.")
                    input("Press any Button to continue...")
            else:
                print("No faculty created yet.")
                input("Press any Button to continue...")

        elif choice == "3":
            name = input("Enter professor name: ")
            age = input("Enter professor age: ")
            professor = FacultyProfessor(name, age, faculty.name)
            faculty.link_professors_to_faculty(professor)

            department_name = input("Enter professor's department name: ")
            department = None
            for dept in faculty.departments:
                if dept.name == department_name:
                    department = dept
                    break
            if department:
                professor.link_department(department)  # Link professor to department
                faculty.link_professors_to_faculty(professor)  # Link professor to faculty
                print(f"{professor.name} linked to {department.name} department.")
            else:
                print(f"Department {department_name} not found.")

                    
        elif choice == "4":
            for professor in faculty.professors:
                if isinstance(professor, FacultyProfessor):  # Check if it's a FacultyProfessor instance
                    professor.read_specific_professor_info()
                else:
                    print("No faculty created yet.")
                    input("Press any Button to continue...")
        
        elif choice == "5":
            for professor in faculty.professors:
                professor.read_specific_professor_info()
                new_age = input("Enter updated age: ")
                professor.update_specific_professor_info(new_age)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
            input("Press any Button to continue...")

main()
