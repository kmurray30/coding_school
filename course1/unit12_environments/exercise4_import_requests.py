# Use the requests library to fetch a webpage

import requests

response = requests.get("https://api.github.com")
print("Status code: " + str(response.status_code))
print("Response preview: " + response.text[:200])

# Expected output:
# Status code: 200
# Response preview: (first 200 chars of JSON response)
