# datetime module works with dates and times

from datetime import datetime

now = datetime.now()
print(now)

# Get just the year
print(now.year)

# Expected output:
# (current date and time)
# (current year)
