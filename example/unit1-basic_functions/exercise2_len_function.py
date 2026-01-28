# Now we're going to get to understand functions a little better.
# input() was a function you just used. 
# Functions are things that perform tasks behind the scenes for you
#   You know they are functions because they have parentheses after them.
#   They somtimes take in inputs, and sometimes return outputs.

# Let's get familiar with another function: len()
# The inputs to a function go inside the parentheses, and the output is returned, able to be assigned to a variable
# len() is a function that returns the length of a string (strings are the values in quotes we have been using so far, like "Hello World")
#   For example, len("abc") returns 3. len("Hello World") returns 11.

# Just like we can set a variable to a value, we can set a variable to the output value of a function.

# For this exercise, I will show you an example usage of len()
#   By ONLY changing the text inside "Hello World" to a different string, have len() return 5.

my_string = "Hello World"
length_of_string = len(my_string)
print(length_of_string)

# Expected output: 5