# PythonLearning

This program generates a password for you based off
a set of rules to help increase security.

I first went about it by doing it step by step
to insure accuracy. After seeing the repeated
steps I decided to use a for loop to use less
lines of code, and to make it look cleaner.

Again after noticing a familiar process with the
for loop. I decided to use list comprehension
which makes my code a lot simpler but the exact
same as the for loops. I quoted out the for loops
as a reference for myself to understand the list
comprehension better

I have both versions of the program to show improvement and my steps through out.

# The actual version is the updatedpw.py file that contains the clean and readable
# code.
EX.
# For Loop

password = [] # create an empty list
for x in range(3): # this will loop over the ASCII code and print 3 upper case letters
    uppercase = chr(random.randint(65,90))
    print(uppercases)

# Now using list comprehension to put all that code in 1 line
-> [expression for item in items]
expression- is what the function thar will happen
item- is what we will get in each iteration
items- is what we will be iterating over
uppercases = [chr(random.randint(65, 90)) for x in range(3)]
