# When to use print debugging vs VS Code debugger

# PRINT DEBUGGING is better when:
# - You want to see values across many iterations
# - You want a permanent record (log file)
# - You're doing quick checks
# - You want to see patterns over time

def sum_with_prints(numbers):
    """Sum numbers with print debugging."""
    total = 0
    for num in numbers:
        total += num
        print(f"DEBUG: Added {num}, total is now {total}")
    return total

print("=== With Print Debugging ===")
result1 = sum_with_prints([1, 2, 3, 4, 5])
print(f"Result: {result1}\n")

# VS CODE DEBUGGER is better when:
# - You want to pause and inspect everything
# - You need to see ALL variables at once
# - You're stepping through complex logic
# - You don't want to modify the code

def sum_with_debugger(numbers):
    """Sum numbers - use debugger to watch it work."""
    # Set a breakpoint on line 36
    # Step through with F10 and watch the Variables panel
    total = 0
    for num in numbers:
        total += num  # Breakpoint here to watch 'num' and 'total' change
    return total

print("=== With VS Code Debugger ===")
print("Set a breakpoint inside sum_with_debugger and watch Variables panel")
result2 = sum_with_debugger([1, 2, 3, 4, 5])
print(f"Result: {result2}")

# BEST PRACTICE: Use both!
# - Print debugging for quick checks
# - VS Code debugger for deep investigation
