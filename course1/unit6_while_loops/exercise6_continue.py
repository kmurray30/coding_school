# continue skips to the next iteration

number = 0
while number < 10:
    number = number + 1
    
    if number % 2 == 0:
        continue
    
    print(number)

# Expected output (only odd numbers):
# 1
# 3
# 5
# 7
# 9
