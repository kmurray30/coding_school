# Strings are immutable - you can't change them, only create new ones

name = "Bobo"

# In theory the following could work, since strings are essentially a sequence of characters.
# In practice it doesn't work because strings are immutable - you can't change them, only create new ones.
name[0] = "p" # Comment when done to suppress the error

# This works - reassigning creates a new string
name = "pobo"
print(name)

# Expected output:
# pobo
