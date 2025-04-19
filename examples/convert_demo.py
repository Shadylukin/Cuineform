"""
Demonstrates base-10 to base-12 conversion and back using functions
from the base12math package.
"""

from base12math import to_base12, from_base12

def run_conversion_demo():
    """Runs the conversion demonstration."""
    print("--- Conversion Demo ---")
    
    test_decimals = [0, 10, 11, 12, 13, 144, 2023]
    print("\nDecimal to Base-12:")
    for dec in test_decimals:
        try:
            b12 = to_base12(dec)
            print(f"{dec:<5} -> {b12}")
        except ValueError as e:
            print(f"Error converting {dec}: {e}")

    test_base12 = ["0", "T", "E", "10", "11", "100", "1207", "te", "1T"] # Corrected 2023, added mixed case, changed 1a to 1T
    print("\nBase-12 to Decimal:")
    for b12_str in test_base12:
        try:
            dec = from_base12(b12_str)
            print(f"{b12_str:<5} -> {dec}")
        except ValueError as e:
            print(f"Error converting '{b12_str}': {e}")

    # Test invalid inputs
    print("\nTesting Invalid Inputs:")
    try:
        from_base12("1G")
    except ValueError as e:
        print(f"Caught expected error for '1G': {e}")
    try:
        to_base12(-5)
    except ValueError as e:
        print(f"Caught expected error for -5: {e}")

if __name__ == "__main__":
    run_conversion_demo()
