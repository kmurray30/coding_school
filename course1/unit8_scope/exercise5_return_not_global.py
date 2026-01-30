# Often better practice: use parameters and return values instead of modifying globals.
# Why? Imagine if your code has 20 functions that all modify the same global variable. It's easy to lose track of what's going on.

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)

# Write your own function that takes two numbers and returns their product
...

print(multiply_numbers(4, 7))

# Expected output:
# 8
# 28
