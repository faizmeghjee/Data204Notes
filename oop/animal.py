# parent class (template for all our animals we create)
class Animal: # class name

    ## class variable
    # animal_kind = 'canine' # class variables are bad as they can be easily reassigned e.g. object.animal_kind = 'new_variable'

    def __init__(self, name: str, animal_kind: str) -> None: # initialisation method 
        self.name = name
        self.animal_kind = animal_kind
        self._age = 0 # a single underscore indicates it is private. a double underscore complete hides it.

    def speak(self): # method
        return 'hello'

    # setter
    def set_age(self, age: int): # allows you to set the attribute 'age'
        # control flow
        self._age = age

    # getter
    def get_age(self): # method for retrieving the attribute 'age'
        return self._age

# creating objects and parsing in the 'name' and 'animal_kind' for each object
pudding = Animal('Pudding', 'cat')
nova = Animal('Nova', 'dog')

# prints the 'animal_kind' for each pet
print(pudding.animal_kind)
print(nova.animal_kind)



class Dog(Animal): # creates a new class using a parent class 'Animal'

    def __init__(self, name: str, animal_kind: str, best_trick: str) -> None:
        super().__init__(name, animal_kind) # super refers to the parentclass (Animal)
        self.best_trick = best_trick # creating a new attribute for class 'Dog'

    def speak(self): # this is overriding the method in the parentclass called 'speak'
        return 'woof!'

kayla = Dog('Kayla', 'dog', 'spin') # must be provided 'name' and 'animal_kind' as parent class reguires them from initialisation

print(kayla.best_trick) # prints the 'best_trick' for object kayla

print(kayla.speak()) 