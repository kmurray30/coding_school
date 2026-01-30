# Functions can be nested. Inner function can access outer function's variables.
# The inner function itself is also a local variable, so it can't be accessed outside of the outer function.

def outer():
    outer_variable = "From outer"
    
    def inner():
        print(outer_variable)
    
    inner()

outer()

# How uncomment the line below to see what happens
# inner()

# Expected output:
# From outer
