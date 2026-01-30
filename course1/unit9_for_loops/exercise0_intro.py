# Unit 8: For Loops
#
# Welcome to the for loops unit! In the previous units, you learned:
# - While loops (repeat until a condition changes)
# - Debugging techniques (print debugging and VS Code debugger)
#
# Now you'll learn about FOR LOOPS, which are perfect for iterating over
# sequences like lists, strings, and ranges of numbers.
#
# DEBUGGING TIP:
# As you work through these exercises, remember the debugging techniques
# from the previous unit! Both print statements and the VS Code debugger
# are excellent tools for understanding how loops work:
#
# - Add print() statements to see what values your loop variable takes
# - Set breakpoints inside loops and use Continue (F5) to jump between iterations
# - Watch the Variables panel to see how values change with each iteration
#
# For loops can be confusing at first, but debugging helps you see exactly
# what's happening at each step!

# Quick comparison: While vs For

# WHILE LOOP (from previous unit):
print("While loop example:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

print()

# FOR LOOP (this unit):
print("For loop example (same result!):")
for counter in range(5):
    print(f"Counter: {counter}")

# Notice: For loops are cleaner when you know exactly how many times to loop!

# TIP: Try setting a breakpoint above and stepping through both loops
# to see how they differ in the debugger. The for loop automatically
# handles the counter increment for you!
