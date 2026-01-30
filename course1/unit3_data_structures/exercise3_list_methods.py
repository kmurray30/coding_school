# Lists are mutable - you can add, remove, and change items

# append() adds an item to the end
shopping_list = ["milk", "eggs"]
shopping_list.append("bread")
print(shopping_list)

# You can change items by assigning to an index
shopping_list[0] = "almond milk"
print(shopping_list)

# remove() removes the first occurrence of an item
shopping_list.remove("eggs")
print(shopping_list)

# len() tells you how many items are in the list
print(len(shopping_list))

# Now practice with your own list
my_numbers = [10, 20, 30]
# Add 40 to the end
...
# Change the first item to 15
...
# Print the list and its length
...
...

# Expected output:
# ['milk', 'eggs', 'bread']
# ['almond milk', 'eggs', 'bread']
# ['almond milk', 'bread']
# 2
# [15, 20, 30, 40]
# 4
