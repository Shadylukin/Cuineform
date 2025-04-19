<a href="https://www.buymeacoffee.com/lukinackc" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px; width: 217px;" >
</a>

# Cuineform: A Duodecimal Pattern Logic Framework

**Cuineform** is a base‑12 (duodecimal) place‑value system and pattern engine, featuring three symbolic operators—§ (emergence/reset), E (even‑halve), and T (trip+1)—that together form a compact automaton for recursive computation, energy‑aware logic, and emergent behavior.

- **Digits:** 0–9, T (10), E (11)
- **Operators:**
  - **T:** Trip+1 (n → 3n+1 if odd)
  - **E:** Even-halve (n → n/2 if even)
  - **§:** Emergence/Reset/Spawn (fires when n ≡ 0 mod 12; triggers recursion, branching, or structural transitions)

---

## Why Cuineform?
- **Pattern-rich:** Base-12 exposes symmetries, cycles, and divisibility hidden in decimal.
- **Symbolic logic:** Operators T, E, and § enable recursive, automaton-like computation and pattern recognition.
- **Physical & digital:** Designed for both software and hardware (see white paper for piezo/energy-harvesting automata).
- **Educational:** A hands-on tool for exploring alternative arithmetic, recursion, and symbolic computation.

---

## Quickstart

```python
from base12math import to_base12, from_base12, add12, mul12

# Convert decimal to base-12 (Cuineform)
print(to_base12(440))   # 308
print(to_base12(280))   # 1E4

# Operators in action (pattern logic)
def cuineform_step(n):
    if n % 12 == 0:
        return '§', n // 12
    elif n % 2 == 0:
        return 'E', n // 2
    else:
        return 'T', 3 * n + 1

n = 48
pattern = []
while n != 1:
    op, n = cuineform_step(n)
    pattern.append(op)
print(' '.join(pattern))  # Example: § E E

# Add and multiply in base-12
print(add12('308', '1E4'))  # 308 + 1E4 = 4EC
print(mul12('308', '2'))    # 308 * 2 = 516
```

---

## Examples
- **Fraction Mandalas:** See `examples/fraction_mandala.py` for repeating cycles of 1/5, 1/7, etc. in base-12.
- **Ancient Structures:** See `examples/ancient_structures.py` for how the Great Pyramid, Stonehenge, and the Parthenon look in Cuineform numbers.
- **Pattern Operators:** See `examples/collatz_demo.py` for symbolic pattern traces using T, E, and §.
- **Compression:** See `examples/compression_demo.py` for how base-12 compresses large numbers more efficiently than decimal.
- **Interactive:** Try `examples/interactive_explorer.py` to experiment with your own numbers and see their Cuineform patterns.

---

## Learn More
- **White Paper:** See `PRIMER.md` for the full theory, operator semantics, and hardware/software blueprint.
- **Open Source:** Contributions, issues, and ideas welcome!

---

## License
MIT
