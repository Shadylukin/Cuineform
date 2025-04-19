"""
Demonstrates base-12 addition and multiplication using functions
from the base12math package.
"""

from base12math import add12, mul12, from_base12 # Import from_base12 for verification

def run_arithmetic_demo():
    """Runs the arithmetic demonstration."""
    print("--- Arithmetic Demo ---")

    pairs_to_test = [
        ("1", "1"),       # 1 + 1 = 2, 1 * 1 = 1
        ("T", "1"),       # 10 + 1 = 11 (E), 10 * 1 = 10 (T)
        ("E", "1"),       # 11 + 1 = 12 (10), 11 * 1 = 11 (E)
        ("T", "E"),       # 10 + 11 = 21 (19), 10 * 11 = 110 (92)
        ("10", "10"),     # 12 + 12 = 24 (20), 12 * 12 = 144 (100)
        ("1T", "2E"),     # Changed A->T, B->E: 22 + 35 = 57 (49), 22 * 35 = 770 (542)
        ("100", "100"),   # 144 + 144 = 288 (200), 144 * 144 = 20736 (10000)
        ("TE", "12"),     # 131 + 14 = 145 (101), 131 * 14 = 1834 (108T)
    ]

    print("\nAddition (Base-12):")
    for a, b in pairs_to_test:
        try:
            result = add12(a, b)
            # Optional: Show decimal equivalent for verification
            dec_a = from_base12(a)
            dec_b = from_base12(b)
            dec_res = from_base12(result)
            print(f"{a} + {b} = {result:<5} ({dec_a} + {dec_b} = {dec_res})")
        except ValueError as e:
            print(f"Error adding {a} + {b}: {e}")

    print("\nMultiplication (Base-12):")
    for a, b in pairs_to_test:
        try:
            result = mul12(a, b)
            # Optional: Show decimal equivalent for verification
            dec_a = from_base12(a)
            dec_b = from_base12(b)
            dec_res = from_base12(result)
            print(f"{a} * {b} = {result:<5} ({dec_a} * {dec_b} = {dec_res})")
        except ValueError as e:
            print(f"Error multiplying {a} * {b}: {e}")

if __name__ == "__main__":
    run_arithmetic_demo()
