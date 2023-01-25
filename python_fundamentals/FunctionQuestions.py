# %%
print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisor(n: int = 1) -> list:
    div_list = []
    for i in range(1, n + 1, 1):
        if n % i == 0:
            div_list.append(i)

    return div_list

divisor(12)

# %%
print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(n1: int, n2: int):
    a = divisor(n2)
    b = divisor(n1)

    if n1 in a:
        return True
    elif n2 in b:
        return True
    else:
        return False

factor(6, 12)

# -------------------------------------------------------------------------------------- #
# %%
print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def letter_loc(word: str):
    return alphabet.index(word.lower())
    
letter_loc('F')

# %%
print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def name_pos(word: str):
    a = ''
    for i in word:
        a = a + str(letter_loc(i))
    return a

name_pos('Faiz')

# %%
print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password_maker(pasw: str):
    a = 0
    b = name_pos(pasw)

    for i in b:
        a += int(i)
    return int(b) - a

password_maker('Faiz')

# -------------------------------------------------------------------------------------- #
# %%
print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def is_prime(number: int):
    if number >= 2:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

is_prime(11)

# %%
print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def is_primee(number: int):
    try:
        number = int(number)     
        if number >= 2:
            for num in range(2, number):
                if number % num == 0:
                    return False
            return True
        return False
    except:
        print('Try Again')
        is_primee(int(input()))

is_primee(input())


# input()
# try:
#     is_prime(int(input()))
# except ValueError:
#     print('Unable to complete, please type a number instead')

# -------------------------------------------------------------------------------------- #
# %%

def isPrimeee(x: int):   
    try: #try except method - good for error handling        
        if x > 1:            
            for i in range(2, x):                
                if x % i == 0:                    
                    return False            
                return True        
            return False    
    except ValueError:        
            print("Try again: ")
            

print(isPrimeee(input("Enter a number: ")))
# %%
