# %%
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:

## print(x[0], x[1], x[2])

y = 5

while y > 0:
    y = y - 1
    print(x[y])

# %%
print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

for num in x:
    if num % 2 == 0:
        print(f'{num} is Even')
    else: 
        print(f'{num} is Odd')


# %%
print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

y = 5

while y > 0:
    y = y - 1
    if x[y] % 2 == 0:
        print(f'{x[y]} is Even')
    else:
        pass

# -------------------------------------------------------------------------------------- #
# %%
print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

first_letters = []

for name in names:
    first_letters.append(name[:1])

print(first_letters)

# %%
print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

space_index = []

for name in names:
    space_index.append(name.index(' '))
##    print(name.find(' '))

print(space_index)

# %%
print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

initials = []

for name in names:
    a = name[0] + ' ' + name.split()[-1][0]
    initials.append(a)

print(initials)

# -------------------------------------------------------------------------------------- #
# %%
print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

for l in list_of_lists:
    a = set(l)
    if len(a) == len(l):
        print(f'{l} has no duplicates')
    else:
        print(f'{l} has duplicates')

# -------------------------------------------------------------------------------------- #
# %%
print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

user_num = int(input('Enter a number greater than 100: '))
try:
    while user_num < 101:
        print(f"{user_num} isn't valid")
        print('Please type a number greater than 100')
        user_num = int(input(''))
except ValueError:
    print('You have not enter a number')


# %%
print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

def isprime(n: int) -> str: 
    if n>1:
        for i in range(2, n//2):
            if(n%i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is neither prime nor composite")

user_num = int(input('Enter a number greater than 100: '))

if user_num < 101:

    while user_num < 101:
        isprime(user_num)
        print(f"{user_num} isn't valid")
        print('Please type a number greater than 100')
        user_num = int(input('Enter a number greater than 100: '))

else:
    isprime(user_num)
    print(f'{user_num} is greater than 100 :)')

# %%

def greeting(user: str = 'Faiz') -> str:
    '''
    Returns Hello followed by your name
    '''
    return 'Hello ' + user

greeting()

# %%
