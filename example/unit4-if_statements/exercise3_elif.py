# What if we have multiple conditions to check?
# We use 'elif' (short for "else if") to check a subsequent condition
# We use 'else' to do one final check if all other conditions are False

grade = 75
if grade >= 90:
    print("A grade!")
elif grade >= 80:
    print("B grade!")
elif grade >= 70:
    print("C grade!")
else:
    print("Below C grade")

# Python checks each condition in order and runs the first True one.

# NOTE: Comment the above code once you've run it

# Your turn: Ask the user for the temperature.
# Print the appropriate message:
# 90+: "Extremely hot!"
# 80-89: "Very hot!"  
# 70-79: "Warm"
# 60-69: "Nice weather"
# Below 60: "Cold!"

...

# Expected output:
# B grade!
# What's the temperature? (wait for input)
# (Appropriate temperature message)
