# Now we can use boolean logic to make decisions in our code!
# The 'if' statement runs code only when a condition is True.

# Basic syntax:
# if condition:
#     code to run if True

age = 18
if age >= 18:
    print("You are an adult!")


# Note that `age >= 18` is a boolean expression that evaluates to True or False
# So you could also write this as:
age = 18
is_adult = age >= 18
if is_adult:
    print("You are an adult!")

# You could even hardcode a boolean value write into the if statement (though you'd never really do this outside of testing)
if True:
    print("This will always run!")

# NOTE: Comment the above code once you've run it

# Notice the indentation! Python uses indentation to group code.
# Everything indented after the 'if' runs when the condition is True.

# Your turn: Ask the user for their age.
# If they are 13 or older, print "You can watch PG-13 movies!"

...

# Expected output:
# What is your age?
# (wait for input)
# You can watch PG-13 movies! OR nothing if they are less than 13
