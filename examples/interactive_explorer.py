"""
Interactive exploration of base-12 (Cuineform) patterns.
Lets the user input a number and see its base-12, Collatz pattern, and fraction cycle.
"""
from base12math import to_base12

def collatz_pattern(n):
    seq = []
    while n != 1 and n > 0:
        if n % 12 == 0:
            seq.append("§")
            n //= 12
        elif n % 2 == 0:
            seq.append("E")
            n //= 2
        else:
            seq.append("T")
            n = 3 * n + 1
    return " ".join(seq)

def base12_fraction_cycle(denom, max_digits=30):
    seen = {}
    n = 1
    digits = []
    pos = 0
    while n and n not in seen and pos < max_digits:
        seen[n] = pos
        n *= 12
        digit = n // denom
        digits.append("0123456789TE"[digit])
        n = n % denom
        pos += 1
    repeat_at = seen.get(n, None)
    return "".join(digits), repeat_at

if __name__ == "__main__":
    print("--- Cuineform Interactive Explorer ---")
    n = int(input("Enter a decimal number: "))
    print(f"Base-12: {to_base12(n)}")
    print(f"Collatz pattern: {collatz_pattern(n)}")
    d = int(input("Enter a denominator for 1/d (decimal): "))
    cycle, repeat = base12_fraction_cycle(d)
    print(f"1/{d} in base-12: 0.{cycle} (cycle length: {len(cycle)})")
    if repeat is not None:
        print(f"  Repeats after {repeat} digits.")
    print("\nChallenge: Try numbers like 1536, 144, 1000, or denominators like 5, 7, 11!")
