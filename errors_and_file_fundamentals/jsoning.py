# %%
import json

# creating a dictionary name 'dog_dict'
dog_dict = {
    'name': 'Nova',
    'favourite_fruit': 'carrots',
    'breed': 'poodle',
    'size': 'toy',
    'age': 3
    }

print(type(dog_dict)) # prints the type of the dictionary which returns '<class 'dict'>'

# json.dumps() # formatted string
# json.dump() # creates a stream object, writes to a file

## examples

# dumps
dog_json_str = json.dumps(dog_dict)
print(type(dog_json_str)) # shows that the json.dumps of the dictionary is now a '<class 'str'>'. Turns it into a formatted string.

# dump
with open('new_file.json', 'w') as json_file: # create a file with name 'new_file.json' in write mode.
    json.dump(dog_dict, json_file) # write the 'dog_dict' to the file 'json_file'

# load (for opening a file)
with open('new_file.json', 'r') as json_file: # open the file 'new_file.json'
    dog = json.load(json_file) # read the file, and assign the information to variable 'dog'.The 'dog' variable will be a dictionary.


# %%
