# Note: in the last assignment, setting list1 = [5, 6, 7] created a new list (somewhere in memory) and assigned it to list1. list2 still points to the original list.

# Use .copy() or slicing to create an independent copy, which is a duplicate entry in memory rather than a reference to the same list.

list1 = [1, 2, 3]
list2 = list1.copy()  # Creates a NEW list

print("Before:")
print("list1: " + str(list1))
print("list2: " + str(list2))

list1.append(4)

print("After modifying list1:")
print("list1: " + str(list1))
print("list2: " + str(list2))

# Another way to copy: slicing
list3 = [5, 6, 7]
list4 = list3[:]
list3.append(8)
print("list3: " + str(list3))
print("list4: " + str(list4))

# Expected output:
# Before:
# list1: [1, 2, 3]
# list2: [1, 2, 3]
# After modifying list1:
# list1: [1, 2, 3, 4]
# list2: [1, 2, 3]
# list3: [5, 6, 7, 8]
# list4: [5, 6, 7]
