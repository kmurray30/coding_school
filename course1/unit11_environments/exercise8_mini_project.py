# Build a GitHub user info fetcher.
# Install dependencies: pip install requests colorama
#
# Your program should:
# 1. Import requests and colorama
# 2. Ask the user for a GitHub username
# 3. Fetch data from https://api.github.com/users/{username}
# 4. If the user exists (status code 200), display their info in color:
#    - Name
#    - Bio
#    - Public repos count
#    - Followers count
#    - Following count
# 5. If user not found, display an error message in red
# 6. Use colorama to make the output colorful

# Expected output:
# GitHub User Info Fetcher
#
# Enter a GitHub username:
# (user types username)
#
# ✓ User found! (in green)
#
# Name: ... (in yellow)
# Bio: ...
# Public repos: ...
# Followers: ...
# Following: ...
#
# OR if not found:
# ✗ User not found! (in red)
