'''
This program will generate a password for you using the
following set of rules to help increase security!
- 3 Upper case letters
- 5 lower case letters
- 2 random numbers
- 2 special charecters
With a total of 12 charecters and these special characters, on average
it would take a hacker 34k years to crack this password based on hive.com
'''
import random  # need to import the random module so the shuffle of charecters is random

# need a function to shuffle the order of characters in password


def shuffle(string):
    # this gives us a temporary list that is a string (sequence of characters)
    templist = list(string)
    # this will shuffle the temporary list which is a mutable sequence
    random.shuffle(templist)
    # need the string values to be joined together to make the password
    # ex. ''.join('ab', 'cd', 'ef') -> ('abcdef')
    return ''.join(templist)


# Generation of the charecters from the set rules begins here
# This will generate a charecter(chr) randomly from the ASCII code of charecters
# 65-90 represents A-Z on ASCII code
uppercase_letter1 = chr(random.randint(65, 90))
uppercase_letter2 = chr(random.randint(65, 90))
uppercase_letter3 = chr(random.randint(65, 90))

# 97-11 represents a-z on ASCII code
lowercase_letter1 = chr(random.randint(97, 122))
lowercase_letter2 = chr(random.randint(97, 122))
lowercase_letter3 = chr(random.randint(97, 122))
lowercase_letter4 = chr(random.randint(97, 122))
lowercase_letter5 = chr(random.randint(97, 122))

# 48-57 is 0-9
number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))

# 32-152 are special charecters
special1 = chr(random.randint(32, 152))
special2 = chr(random.randint(32, 152))

# time to put all the characters together to make the password
password = (uppercase_letter1 + uppercase_letter2 + uppercase_letter3 + lowercase_letter1 + lowercase_letter2 +
            lowercase_letter3 + lowercase_letter4 + lowercase_letter5 + number1 + number2 + special1 + special2)

# shuffle the password around to randomize it
generated_pw = shuffle(password)

# print/display the password
print(generated_pw)

'''
for x in range(3):
    uppercases = chr(random.randint(65, 90))
    print(uppercases)
'''
uppercases = [chr(random.randint(65, 90)) for x in range(3)]
print(uppercases)

'''
for y in range(5):
    lowercases = chr(random.randint(97, 122))
    print(lowercases)
'''
lowercases = [chr(random.randint(97, 122)) for y in range(5)]
print(lowercases)

'''
for z in range(2):
    numbers = chr(random.randint(48, 57))
    print(numbers)
'''
numbers = [chr(random.randint(48, 57)) for z in range(2)]
print(numbers)

'''
for n in range(2):
    specials = chr(random.randint(32, 152))
    print(specials)
'''
specials = [chr(random.randint(32, 47)) for n in range(2)]
print(specials)

generation = (uppercases + lowercases + numbers + specials)
secrecy = shuffle(generation)
print(secrecy)
