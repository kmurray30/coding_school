# Tuples are immutable, lists are mutable

mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)

# This works
mutable_list[0] = 100
print(mutable_list)

# This doesn't work - uncomment to see the error
# immutable_tuple[0] = 100

# But you can reassign the whole tuple
immutable_tuple = (100, 2, 3)
print(immutable_tuple)

# Expected output:
# [100, 2, 3]
# (100, 2, 3)
