# Create a function that takes in a list and returns two items (via a tuple):

# - A reference to the original list, but with each element incremented by 1.
# - A reference to a backup copy of the original list.

def update_with_backup(list) -> tuple[list, list]:
    ...
    return (list, backup_list)

test_list = [1, 2, 3]
updated_list, backup_list = update_with_backup(test_list)
print(updated_list)
print(backup_list)

# Expected output:
# [2, 3, 4]
# [1, 2, 3]
