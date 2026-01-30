# Now you add the debug print statements
# See if you can find the bug in the code and fix it

def calculate_total(item_price, quantity, tax_percent):
    """Calculate total cost including tax."""
    
    subtotal = item_price * quantity
    
    tax_amount = subtotal * tax_percent
    
    total = subtotal + tax_amount
    
    return total

# Test it
result = calculate_total(25, 3, 10)
print(f"Total: ${result}")

# Expected output (after fixing the bug):
# <your debug prints here>
# Total: $82.5
