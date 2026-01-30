# Lists are mutable - you can change them in place

numbers = [1, 2, 3, 4, 5]
print("Before: " + str(numbers))

numbers[0] = 100
print("After: " + str(numbers))

# Try changing another element
...

# Expected output:
# Before: [1, 2, 3, 4, 5]
# After: [100, 2, 3, 4, 5]
# (your result)
