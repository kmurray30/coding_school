# Accumulator with for loop instead of while

total = 0
for number in range(1, 11):
    total = total + number

print("Sum of 1-10: " + str(total))

# Create a function that calculates the product of 1-n (or in other words the factorial of n)
...

print("Product of 1-5: " + calculate_product(5))

# Expected output:
# Sum of 1-10: 55
# Product of 1-5: 120
