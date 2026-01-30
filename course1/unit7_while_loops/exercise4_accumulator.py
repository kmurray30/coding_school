# Accumulator pattern - build up a total

total = 0
number = 1

while number <= 10:
    total = total + number
    number = number + 1

print("Sum of 1-10: " + str(total))

# Try multiplying instead of adding
...

# Expected output:
# Sum of 1-10: 55
# (your result)
