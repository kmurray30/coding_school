# Find the bug using VS Code debugger

# This function has a bug - use the debugger to find it
# Don't use print statements this time - use breakpoints!

# INSTRUCTIONS:
# 1. Set a breakpoint at line 32 (inside the function)
# 2. Start debugging
# 3. Look at the Variables panel to see 'total' and 'count'
# 4. Use Step Over (F10) to move through the loop
# 5. Watch how 'total' and 'count' change
# 6. Find the bug!

def calculate_average(numbers):
    """Calculate average of positive numbers only."""
    total = 0
    count = 0
    
    for number in numbers:
        if number > 0:
            total += number
        count += 1
    
    if count == 0:
        return 0
    
    average = total / count
    return average

# This should return 25.0 (because (10+20+30+40)/4 = 25)
# But it will be wrong because of the bug
test_numbers = [10, -5, 20, 0, 30, -15, 40]
result = calculate_average(test_numbers)

print(f"Average: {result}")

# Expected output (after fixing the bug):
# Average: 25.0