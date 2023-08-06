class Professor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read_specific_professor_info(self):
        print(f"Professor: {self.name}, age: {self.age}")

    def update_specific_professor_info(self, new_age):
        self.age = new_age
        print(f"Updated age for {self.name}: {self.age}")


class FacultyProfessor(Professor):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty


class FacultyProfessor(Professor):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty
        self.department = None 

    def link_department(self, department):
        self.department = department
        print(f"{self.name} linked to {department.name} department.")
