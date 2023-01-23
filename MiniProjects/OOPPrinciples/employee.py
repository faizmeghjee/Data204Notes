import person


class Employee(person.Person):
    def __init__(self, fname, lname, department):
        self._department = department
        super().__init__(fname, lname)

    def print(self):
        print(f'Department: {self._department}', end=' ')
        super().print()
