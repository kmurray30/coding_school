# List methods mutate the list in place

fruits = ["apple", "banana"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

last_fruit = fruits.pop()
print("Popped: " + last_fruit)
print(fruits)

# Play around with the list methods to get a feel for how they work.

# Expected output:
# ['apple', 'banana']
# ['apple', 'banana', 'orange']
# ['apple', 'orange']
# Popped: orange
# ['apple']
