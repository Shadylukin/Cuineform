"""
Demonstrates the effectiveness of base-12 (Cuineform) for numeric compression.
Shows how large numbers require fewer digits in base-12 than in base-10 or base-2.
"""
from base12math import to_base12

def digit_count(n, base):
    """Returns the number of digits needed to represent n in the given base."""
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= base
        count += 1
    return count

def compare_compression(numbers):
    print(f"{'Decimal':>20} | {'Base-10':>7} | {'Base-12':>7} | {'Base-2':>7} | {'Base-12 String':>15}")
    print("-" * 70)
    for n in numbers:
        dec_str = str(n)
        b12_str = to_base12(n)
        b2_str = bin(n)[2:]
        print(f"{dec_str:>20} | {len(dec_str):>7} | {len(b12_str):>7} | {len(b2_str):>7} | {b12_str:>15}")

if __name__ == "__main__":
    numbers = [
        0,
        123,
        1000,
        1000000,
        123456789,
        2**32,
        10**18,
        12**12,  # A power of 12 for fun
    ]
    compare_compression(numbers)
    print("\nNote: Fewer digits = more compact representation. Base-12 is always shorter than base-10 for large numbers!")
    print("Try using base-12 for data encoding, pattern discovery, or just for fun!")
