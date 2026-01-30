# Find the bug using print debugging

# This function has a bug - add debug prints to find it

def determine_grade(score):
    """Return letter grade for a numeric score."""
    # TODO: Add debug prints to see which branch is taken
    
    if score >= 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return grade

# Test it - one of these will show the bug
test_scores = [95, 85, 80, 75, 65, 55]

for score in test_scores:
    grade = determine_grade(score)
    print(f"Score {score} -> Grade {grade}")

# Expected output:
# Score 95 -> Grade A
# Score 85 -> Grade B
# Score 80 -> Grade B
# Score 75 -> Grade C
# Score 65 -> Grade D
# Score 55 -> Grade F
