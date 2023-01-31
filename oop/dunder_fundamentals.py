# %% Dunder Methods
class Location:
    def __init__(self, lat, lon) -> None:
        self.latitude = lat
        self.longitude = lon

    def __str__(self) -> str: # Changes the object into a 'str'(string) representation of it.
        return f'This is the latitude: {self.latitude}\nThis is the longitude: {self.longitude}'

bham_academy = Location(52.488, -1.887)
print(bham_academy) # returns This is the latitude: 52.488 This is the longitude: -1.887

## Some basic examples of dunder methods:
# __new__(self) return a new object (an instance of that class). It is called before __init__ method.
# __init__(self) is called when the object is initialized. It is the constructor of a class.
# __del__(self) for del() function. Called when the object is to be destroyed. Can be used to commit unsaved data or close connections.
# __repr__(self) for repr() function. It returns a string to print the object. Intended for developers to debug. Must be implemented in any class.
# __str__(self) for str() function. Return a string to print the object. Intended for users to see a pretty and useful output. If not implemented, __repr__ will be used as a fallback.
# __bytes__(self) for bytes() function. Return a byte object which is the byte string representation of the object.
# __format__(self) for format() function. Evaluate formatted string literals like % for percentage format and ‘b’ for binary.
# __lt__(self, anotherObj) for < operator.
# __le__(self, anotherObj) for <= operator.
# __eq__(self, anotherObj) for == operator.
# __ne__(self, anotherObj) for != operator.
# __gt__(self, anotherObj)for > operator.
# __ge__(self, anotherObj)for >= operator.



# This makes everything within the If statement only run if the file is run directly.
if __name__ == '__main__':  # won't be run if the file is imported into another file.
    print('This is the python file: ' + __name__) # returns __main__ if ran directly from file.
    print(type(bham_academy))

# %%
