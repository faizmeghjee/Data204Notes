class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')

    @property
    def first_name(self):
        print('In get method')
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print('In set method')
        self._first_name = new_first_name
