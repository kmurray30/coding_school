# and requires BOTH conditions to be True

print(True and True)
print(True and False)
print(False and True)
print(False and False)

age = 25
has_license = True
is_organ_donor = False

print("\nAge / License / Organ Donor:")
print(age >= 18 and has_license)
print(age >= 18 and is_organ_donor)
print(age >= 18 and has_license and is_organ_donor)

# Try your own
...

# Expected output:
# True
# False
# False
# False
# 
# Age / License / Organ Donor:
# True
# False
# False
# (your result)
