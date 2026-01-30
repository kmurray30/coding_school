# While loops ask "are we there yet?" until the answer changes.
# Just like if statements, treat the while lines as lines like any other line of code that runs sequentially.

count = 1
while count <= 3:
    print(count)
    count = count + 1
print("Done!")

# The order of operations of the code above is:
#    1. count = 1
#    2. while count <= 3: (1 <= 3 is true, so run the code block)
#    3.     print(count) (prints 1)
#    4.     count = count + 1 (count is now 2)
#    4. while count <= 3: (2 <= 3 is true, so run the code block)
#    5.     print(count) (prints 2)
#    6.     count = count + 1 (count is now 3)
#    7. while count <= 3: (3 <= 3 is true, so run the code block)
#    8.     print(count) (prints 3)
#    9.     count = count + 1 (count is now 4)
#    10. while count <= 3: (4 <= 3 is false, so stop the loop)
#    11. print("Done!") (prints "Done!")

# Expected output:
# 1
# 2
# 3
# Done!
