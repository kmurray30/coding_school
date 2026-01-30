# Converting float to int cuts off the decimal. No rounding.

price = 9.99
price_int = int(price)
print(price_int)

# Try with another number
another_float = ...
print(int(another_float))

# Expected output:
# 9
# (your result, decimal chopped off)
