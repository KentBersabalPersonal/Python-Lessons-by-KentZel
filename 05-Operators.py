a = 10
b = 3

print("\nSum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

# OUTPUT IS:
# Sum: 13
# Difference: 7
# Product: 30
# Quotient: 3.3333333333333335
# Floor Division: 3
# Remainder: 1

# a / b   -> "true division" — ALWAYS gives a decimal result, even if both numbers are whole (10 / 3 = 3.333...)
# a // b  -> "floor division" — cuts off the decimal, giving a whole number result (this is what C/C++'s "/" does for ints)
