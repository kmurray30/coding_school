# Nested loops - loop inside a loop

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
