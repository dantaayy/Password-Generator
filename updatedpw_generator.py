'''
This is the updated version of the password
generator. For cleaner, and more readable code.
This version will just use list comprehension
to gen the charecters needed for our password
based on a set of rules
RULES:
- 3 Upper case letters
- 5 lower case letters
- 2 random numbers
- 2 special charecters
'''
import random
# First make a funtion that will shuffle the order of our charecterss randomly


def shuffle(string):
    # need a templist from a string of charecters
    templist = list(string)
    # randomly shuffle our temp list
    random.shuffle(templist)
    # need the charecters to be joined together and returned
    return ''.join(templist)


# This will get our uppercases from the ASCII code
uppercases = [chr(random.randint(65, 90)) for x in range(3)]

# Lowercases from ASCII code
lowercases = [chr(random.randint(97, 122)) for x in range(5)]

# Numbers from ASCII
numbers = [chr(random.randint(48, 57)) for x in range(2)]

# Special Charecters from ASCII
special = [chr(random.randint(32, 47)) for x in range(2)]

# Combine all the charecters together
password = uppercases + lowercases + numbers + special

# Randomly shuffle all the charecters to generate a strong password
generated = shuffle(password)
print(generated)
