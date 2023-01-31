from datetime import date

# %%
## Functions

def function_name(arguments):
    # block_of_code
    pass

# e.g. one parameter

def introduction(name): # takes one arguement and will print the message shown in the block of code
    '''Introduces a person given their name'''
    print(f'Hello! my name is {name}')

# e.g. no parameter

def error_message(): # takes no arguements as the block of code doesn't require anything from the user
    '''Prints an error message'''
    print('We have encountered an error')

# e.g. multiple parameters

def get_age(birth_year, birth_month, birth_day): # takes 3 arguements
    '''Calculates age (in years) based on birth year, month and day'''
    birth_date = date(birth_year, birth_month, birth_day) # converts the three arguements given into a date
    age = date.today() - birth_date # calculates the age in days
    age_years = age.days / 365.2425 # 
    return age_years

get_age(1997, 11, 30)

# %%
## For Loops

# looping a list
fruits = ['apple', 'banana', 'mango', 'cherry'] # creating a list called fruits
for x in fruits: # iterating through the list of fruits, where i represents each element
    print(x) # prints each element as it iterates through

# looping through a string

for x in 'banana': # iterates through each letter in the word 'banana'
    print(x) # prints each letter

# the string banana can also be assigned to a variable and iterated through e.g.
yellow_fruit = 'banana'
for x in yellow_fruit:
    print(x)

# for loops with a condition
for x in fruits:
    print(x)
    if x == 'banana': # if the iteration is equal to the word banana, if block will run
        break  # this exits the loop

for x in fruits:
    if x == 'banana':
        continue # this statement allows us to stop the current iteration and continue to next
    print(x)

# range() function

for x in range(6): # this loop returns a sequence of numbers starting from 0 and ends at 5
    print(x)

for x in range(2, 6): # looping starting from 2 up to 6 but no including 6
    print(x)

for x in range(2, 30, 3): # looping from 2 to 30, with increments of 3
    print(x)

# %%

stu_a = ['Alex', 'Briana', 'Cheri', 'Daniele']
stu_b = ['Dora', 'Minerva', 'Alexa', 'Obie']

for student in stu_a:
    stu_b.append(student)
    print(student)

# %%

word = 'Sarah'

def password_generator(name):
    # password = name[1:] + name[0]
    password = ''
    for i in range(len(name)):
        password += name[i-1]
    return password

password_generator(word)

# %%
