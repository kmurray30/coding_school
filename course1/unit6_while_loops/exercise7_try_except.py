# try/except lets you handle errors gracefully instead of crashing
# This is also called "exception handling"

# Without try/except - this would crash
print("Example 1: Without error handling")
# Uncomment the line below to see it crash:
# result = int("hello")
print("(Skipping the crash for now)\n")

# With try/except - program continues even if there's an error
print("Example 2: With try/except")
try:
    result = int("hello")
    print("Conversion succeeded!")
except ValueError:
    print("Can't convert 'hello' to an integer")
    print("But the program keeps running!\n")

# Another example with valid input
print("Example 3: No error occurs")
try:
    result = int("42")
    print(f"Conversion succeeded! Result: {result}")
except ValueError:
    print("This won't run because there was no error\n")

# You can use this to protect risky operations
print("\nExample 4: Protecting risky operations")
user_input = "not a number"
try:
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print(f"'{user_input}' is not a valid number")

# Different types of errors
print("\nExample 5: Different error types")
my_list = [1, 2, 3]
try:
    print(my_list[10])  # Index out of range
except IndexError:
    print("Index doesn't exist in the list")

# You can catch multiple error types. Try changing the test_value to 0 and see what happens.
print("\nExample 6: Multiple except blocks")
test_value = "abc"
try:
    result = int(test_value)
    division = 10 / result
except ValueError:
    print(f"'{test_value}' is not a number")
except ZeroDivisionError:
    print("Can't divide by zero")

# Now try your own - ask user for a number and convert it
# Use try/except to handle the case where they don't enter a number
print("\nYour turn:")
user_value = input("Enter a number: ")
try:
    converted = int(user_value)
    print(f"Success! Your number doubled is {converted * 2}")
except ValueError:
    print(f"'{user_value}' is not a valid number")

# Expected output (if user enters "42"):
# Example 1: Without error handling
# (Skipping the crash for now)
# 
# Example 2: With try/except
# Can't convert 'hello' to an integer
# But the program keeps running!
# 
# Example 3: No error occurs
# Conversion succeeded! Result: 42
# 
# Example 4: Protecting risky operations
# 'not a number' is not a valid number
# 
# Example 5: Different error types
# Index doesn't exist in the list
# 
# Example 6: Multiple except blocks
# 'abc' is not a number
# 
# Your turn:
# Enter a number: 42
# Success! Your number doubled is 84
