# Practice setting breakpoints and using the debugger

# INSTRUCTIONS:
# 1. Set a breakpoint on line 16 (click in the left margin)
# 2. Press F5 to start debugging
# 3. When it pauses, look at the Variables panel
# 4. Press F10 (Step Over) or use the debugger UI to move through each line
# 5. Watch the Variables panel as values change
# 6. When you get to line 19, press F11 (Step Into) or use the debugger UI to step into the function call

def calculate_area(length, width):
    """Calculate area of a rectangle."""
    area = length * width
    return area

# Set breakpoint here (line 16)
length = 10
width = 5
area = calculate_area(length, width)
print(f"Area: {area}")

# Expected: You'll see length, width, and area appear in Variables panel as you step
