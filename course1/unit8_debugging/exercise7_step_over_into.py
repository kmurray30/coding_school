# Practice Step Over vs Step Into

# INSTRUCTIONS:
# 1. Set a breakpoint on line 24
# 2. Start debugging (F5)
# 3. When it pauses, press F10 (Step Over) - watch what happens
# 4. Restart debugging
# 5. This time press F11 (Step Into) - notice the difference!

def add(a, b):
    """Add two numbers."""
    result = a + b
    return result

def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    return result

# Set breakpoint here
x = 10
y = 5

sum_result = add(x, y)  # Try Step Over (F10), then try Step Into (F11)
product = multiply(x, y)

print(f"Sum: {sum_result}")
print(f"Product: {product}")

# Step Over (F10): Executes add() completely, stays in this file
# Step Into (F11): Jumps INTO the add() function so you can see inside
