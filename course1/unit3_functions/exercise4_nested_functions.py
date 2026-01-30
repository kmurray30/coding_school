# Functions can be nested. Inner function runs first.

# This runs len() on the result of input()
print("Type something:")
print(len(input()))

# Same thing, but broken into steps
print("Type something else:")
user_input = input()
input_length = len(user_input)
print(input_length)

# Both approaches work. Second is more readable.

# Expected output:
# Type something:
# (user types)
# (length)
# Type something else:
# (user types)
# (length)
