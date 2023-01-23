import person


class Customer(person.Person):
    def __init__(self, fname, lname, address):
        self._address = address
        super().__init__(fname, lname)

    def print(self):
        print(f'Address: {self._address}', end=' ')
        super().print()
