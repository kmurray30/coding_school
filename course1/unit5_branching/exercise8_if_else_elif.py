# if, elif, else handle multiple cases.
# elif is short for "else if", or "if the previous conditions were not met, check this condition"
# else runs if and only if all prior conditions are not met.
# Note that if any of the conditions are met, the remaining elif and else blocks will not be checked.

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Write your own multi-branch logic
...

# Expected output:
# Grade: B
# (your output)
