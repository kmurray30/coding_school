# Debug and fix a mutable default argument bug.
# This code has a subtle bug.
# The goal of the code is to end up with two lists, one with "apples" and one with "bananas".

def create_list_with_item(item, new_list=[]):
    new_list.append(item)
    return new_list

list1 = create_list_with_item("apples")
print("List 1: " + str(list1))

list2 = create_list_with_item("bananas")
print("List 2: " + str(list2))

# Expected output (after fixing the bug):
# List 1: ['apples']
# List 2: ['bananas']

# What does this behavior tell you about creating lists inside function parameters?

# Explanation: -->                                                                                                 a list is created once when the function is defined, not per call.
