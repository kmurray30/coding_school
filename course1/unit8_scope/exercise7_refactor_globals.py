# Refactor bad code that uses global variables.
# Here's the bad version that modifies a global:

# score = 0
# 
# def multiply_score(multiplier):
#     global score
#     score = score * multiplier
#
# score = 1  # Start at 1 for multiplication
# multiply_score(2)
# multiply_score(3)
# print(score)  # Should print 6

# Rewrite this WITHOUT using global variables.
# Use function parameters and return values instead.
# The output should still be 6.

# Your refactored version here:
