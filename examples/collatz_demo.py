"""
Demonstrates Collatz sequence pattern operators in base-12 (Cuineform style).
"""
from base12math import to_base12

def collatz_pattern(n):
    seq = []
    while n != 1:
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

if __name__ == "__main__":
    start = 48  # 40₁₂
    print(f"Collatz pattern for {to_base12(start)}₁₂ ({start}₁₀):")
    print(collatz_pattern(start))
    # Try a few more
    for n in [12, 24, 36, 60]:
        print(f"n = {to_base12(n)}₁₂ ({n}₁₀): {collatz_pattern(n)}")
