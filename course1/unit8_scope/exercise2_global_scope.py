# Global variables are accessible everywhere

global_variable = "I'm global"

def my_function():
    print(global_variable)

my_function()
print(global_variable)

# Expected output:
# I'm global
# I'm global
