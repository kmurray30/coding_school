# Install faker first: pip install faker

from faker import Faker

fake = Faker()

print("Fake name: " + fake.name())
print("Fake email: " + fake.email())
print("Fake address: " + fake.address())
print("Fake company: " + fake.company())

# Generate multiple fake names
print("\nFive fake names:")
for i in range(5):
    print(fake.name())

# Expected output:
# (randomly generated fake data)
