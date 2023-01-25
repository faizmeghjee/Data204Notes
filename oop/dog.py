class Dog: # class name

    animal_kind = 'canine' # class variable

    def __init__(): # method
        pass
    
    def bark(self): # method
        return 'woof'

# creating objects using the Dog class
princess_kiki = Dog() 
sir_max = Dog() 

# printing the method for each object
print(princess_kiki.bark())
print(sir_max.bark())

# assigning "princess_kiki a different class variable for "animal_kind"
princess_kiki.animal_kind = 'cat'