# Boolean operators have an order of operations: not, then and, then or
# Just like in math, parentheses override the default order.

# Order: not first, then and, then or
print("Without parentheses:")
result1 = True or False and False
print(f"True or False and False = {result1}")  # and happens first: False and False = False, then True or False = True

result2 = not True or False
print(f"not True or False = {result2}")  # not happens first: not True = False, then False or False = False

result3 = True and not False
print(f"True and not False = {result3}")  # not happens first: not False = True, then True and True = True

result4 = False or True and not False
print(f"False or True and not False = {result4}")  # not first: not False = True, then and: True and True = True, then or: False or True = True

print("\nWith parentheses (override default order):")
result5 = (True or False) and False
print(f"(True or False) and False = {result5}")  # parentheses first: True or False = True, then True and False = False

result6 = not (True or False)
print(f"not (True or False) = {result6}")  # parentheses first: True or False = True, then not True = False

result7 = True and (not False)
print(f"True and (not False) = {result7}")  # Same as without parentheses since not has highest precedence anyway

# Expected output:
# Without parentheses:
# True or False and False = True
# not True or False = False
# True and not False = True
# False or True and not False = True
# 
# With parentheses (override default order):
# (True or False) and False = False
# not (True or False) = False
# True and (not False) = True
