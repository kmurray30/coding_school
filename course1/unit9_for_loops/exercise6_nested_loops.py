# Nested loops - loop inside a loop

# DEBUGGING TIP:
# Nested loops can be confusing! Here's how to debug them effectively:
# 1. Set a breakpoint at the outer loop (line 9)
# 2. Watch the Variables panel - you'll see both 'i' and 'j' changing
# 3. Notice how 'j' cycles through 1,2,3 for EACH value of 'i'
# 4. Use Step Over (F10) to see the flow, or add print statements like:
#    print(f"DEBUG: i={i}, j={j}")

for i in range(1, 4):
    for j in range(1, 4):
        print(str(i) + " x " + str(j) + " = " + str(i * j))
    print("---")

# Expected output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ---
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ---
