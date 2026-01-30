# Find the bug using print debugging

# This function should sum even numbers from 1 to max_number (inclusive)
# But there's a bug - add debug prints to find it

def sum_even_numbers(max_number):
    """Sum all even numbers from 1 to max_number."""
    
    total = 0
    current = 1
    
    while current < max_number:
        if current % 2 == 0:
            total += current
        current += 1
    
    return total

# This should return 30 (2+4+6+8+10)
n = 10
result = sum_even_numbers(n)
print(f"Sum of even numbers 1-{n}: {result}")

# Expected output (after fixing the bug):
# <your debug prints here>
# Sum of even numbers 1-10: 30
