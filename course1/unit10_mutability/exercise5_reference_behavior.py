# Two variables can point to the same list. Modifying one affects both.

list1 = [1, 2, 3]
list2 = list1  # Both point to the SAME list

print("Before:")
print("list1: " + str(list1))
print("list2: " + str(list2))

list1.append(4)

print("After modifying list1:")
print("list1: " + str(list1))
print("list2: " + str(list2))

# Now assign a new value to list1
list1 = [5, 6, 7]

# What do you think will happen when we print list2? (see explanation in next assignment)
print("list2: " + str(list2))

# Expected output:
# Before:
# list1: [1, 2, 3]
# list2: [1, 2, 3]
# After modifying list1:
# list1: [1, 2, 3, 4]
# list2: [1, 2, 3, 4]
# ???
