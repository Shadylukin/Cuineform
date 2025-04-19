"""
Demonstrates base-12 fraction expansions and repeating cycles (mandalas).
"""
from base12math import to_base12

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
    print("--- Fraction Mandala Cycles in Base-12 ---")
    for d in [5, 7, 8, 11]:
        cycle, repeat = base12_fraction_cycle(d)
        print(f"1/{d}₁₀ in base-12: 0.{cycle} (cycle length: {len(cycle)})")
        if repeat is not None:
            print(f"  Repeats after {repeat} digits.")
