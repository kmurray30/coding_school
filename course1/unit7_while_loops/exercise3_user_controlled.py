# Loop until user says to stop

command = ""
while command != "quit":
    print("Type 'quit' to exit, or anything else to continue:")
    command = input()
    
    if command != "quit":
        print("Still going...")

print("Goodbye!")

# Expected output:
# Type 'quit' to exit, or anything else to continue:
# (user types something)
# Still going...
# Type 'quit' to exit, or anything else to continue:
# (user types 'quit')
# Goodbye!
