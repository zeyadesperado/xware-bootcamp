class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def read_specific_department_info(self):
        print(f"id: {self.id}, name: {self.name}")

    def update_specific_department_info(self, new_name):
        self.name = new_name
        print(f"The name has been updated to {self.name} sucessfuly")


class FacultyDepartment(Department):
    def __init__(self, id, name, faculty):
        super().__init__(id, name)
        self.faculty = faculty
# print(help(FacultyDepartment))

class ProfessorDepartment(Department):
    def __init__(self, id, name, professor):
        super().__init__(id, name)
        self.professor = professor