# Print debugging - adding print() statements to see what's happening

# One of the simplest debugging techniques: add print() to see variable values

def calculate_discount(price, discount_percent):
    """Calculate final price after discount."""
    print(f"DEBUG: price={price}, discount={discount_percent}%")
    
    discount_amount = price * (discount_percent / 100)
    print(f"DEBUG: discount_amount={discount_amount}")
    
    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")
    
    return final_price

# Run it and watch the debug output
result = calculate_discount(100, 20)
print(f"\nFinal result: ${result}")

# Expected output:
# DEBUG: price=100, discount=20%
# DEBUG: discount_amount=20.0
# DEBUG: final_price=80.0
#
# Final result: $80.0
