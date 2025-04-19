"""
Demonstrates pattern operators in base-12 (Cuineform style).
"""
from base12math import to_base12, from_base12

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

def cuineform_step(n):
    if n % 12 == 0:
        return '§', n // 12
    elif n % 2 == 0:
        return 'E', n // 2
    else:
        return 'T', 3 * n + 1

def cuineform_pattern_trace(n):
    pattern = []
    while n != 1:
        op, n = cuineform_step(n)
        pattern.append(op)
    return pattern

if __name__ == "__main__":
    start = 48  # 40₁₂
    print(f"Pattern for {to_base12(start)}₁₂ ({start}₁₀):")
    print(collatz_pattern(start))
    # Try a few more
    for n in [12, 24, 36, 60]:
        print(f"n = {to_base12(n)}₁₂ ({n}₁₀): {collatz_pattern(n)}")

    # Example usage:
    n = 48
    print(f"Pattern trace for {n} (decimal):", ' '.join(cuineform_pattern_trace(n)))
    # Try with a base-12 input
    n_b12 = '308'  # 440 decimal
    n_dec = from_base12(n_b12)
    print(f"Pattern trace for {n_b12}₁₂ ({n_dec}₁₀):", ' '.join(cuineform_pattern_trace(n_dec)))
