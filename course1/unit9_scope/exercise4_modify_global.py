# Use global keyword to modify global variables from inside a function

counter = 0

def increment():
    global counter
    counter = counter + 1

print("Before: " + str(counter))
increment()
print("After: " + str(counter))
increment()
print("After again: " + str(counter))

# Bonus: See what happens when you remove the global keyword

# Expected output:
# Before: 0
# After: 1
# After again: 2
