# Just like in math, boolean operations have an order of operations (precedence).
# Order from highest to lowest precedence:
# 1. Parentheses ()
# 2. not
# 3. and
# 4. or

# Examples - predict what these will output:
print(True or False and False)  # True - `or` has lower precedence than `and`
print((True or False) and False)  # False - parentheses change the order
print(not False or True)  # True - `not` has higher precedence than `or`
print(not (False or True))  # False - parentheses change the order

# NOTE: Comment the above code once you've run it

print((True or False) and False)
print(True or False and False)

# Complex example:
has_license = True
has_permit_and_guardian = False
is_sober = False

# Without parentheses - does the output make sense? If not, see if you can fix it with parentheses.
can_drive = has_license or has_permit_and_guardian and is_sober
print("Can drive: ", can_drive)

# NOTE: Comment the above code once you've run it

# Your turn: Create a complex boolean expression that checks if someone can vote.
# Rules: Must be 18 or older AND either be a citizen OR have been a resident for 5+ years
# Use variables for age, is_citizen, and years_resident

age = ...
is_citizen = ...
years_resident = ...

can_vote = ...

print("Can vote:", can_vote)

# Expected output:
# Age? (int)
#   (wait for input)
# Is citizen? (True/False)
#   (wait for input)
# Years resident? (int)
#   (wait for input)
# Can vote: (True/False depending on your values)
#
# Note: What cases should you test to make sure your code is working perfectly? Thinking through all of the
#   edge cases and testing them is the key to being a great programmer. Congrats! You're already thinking like one!
