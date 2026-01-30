# break exits the loop immediately

count = 1
while True:
    print(count)
    if count >= 5:
        break
    count = count + 1

print("Done!")

# Expected output:
# 1
# 2
# 3
# 4
# 5
# Done!
