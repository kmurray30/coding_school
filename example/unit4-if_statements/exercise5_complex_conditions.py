# You can use complex boolean logic in if statements!

age = 25
has_job = True
credit_score = 720

# Check if someone qualifies for a loan
if (age >= 18 and has_job) and credit_score >= 650:
    print("Loan approved!")
elif age >= 18 and credit_score >= 750:
    print("Loan approved despite no job!")
else:
    print("Loan denied.")

# NOTE: Comment the above code once you've run it

# Your turn: Create a game admission checker.
# Rules: 
# - Must be 13+ to play
# - If under 18, must have parent permission OR be with a friend who is 18+
# - Must have paid (yes/no)
# Ask for: age, parent permission, friend age (if applicable), paid status

...

# Expected output:
# Age? (int)
#   (wait for input)
# Parent permission? (True/False)
#   (wait for input)
# With a friend? (True/False)
#   (wait for input)
# Friend age? (int) (ONLY ASK IF WITH A FRIEND)
#   (wait for input)
# Paid? (True/False)
#   (wait for input)
# Welcome young one and parent! OR Welcome young one and friend! OR Sorry lil guy, go home!
