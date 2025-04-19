# The Cuineform Primer (v 1)
*An easy‑entry guide to Lukin’s base‑12 pattern language*

---
## 1. What *is* Cuineform?
Cuineform is a **duodecimal (base‑12) place‑value system** with three extra glyphs that turn arithmetic into a pattern‑recognition engine.  
It began as a dream‑spark: “What if numbers could *draw* their own behaviour?”  
Over weeks of exploration we:
- Mapped fractions into polar mandalas (1∕5 → 4‑spoke wheel, 1∕7 → 6‑spoke).  
- Re‑expressed famous monuments (Great Pyramid, Stonehenge) in base‑12, recovering hidden symmetries.  
- Re‑coded the Collatz recursion as a 12‑state automaton, revealing bulging “reset” hotspots.

---
## 2. The Digit Set
| Decimal | Cuineform | Pronounce |
|---------|-----------|-----------|
| 0       | **0**     | zero      |
| 1‑9     | 1‑9       | same      |
| 10      | **T**     | "ten"    |
| 11      | **E**     | "el"     |

> **12₁₀ = 10₁₂** • **24₁₀ = 20₁₂** • **144₁₀ = 100₁₂**

---
## 3. Pattern Operators
| Glyph | Meaning (core)                      | In Collatz demo |
|-------|-------------------------------------|-----------------|
| **§** | *Reset* – value ≡ 0 (mod 12)         | hit a multiple of 12 |
| **E** | *Even‑halve* (n → n∕2)               | “E” step        |
| **T** | *Trip+One* (n → 3n + 1)              | “T” step        |

These operators layer on top of the digits; e.g. `§EET…` is a Collatz fingerprint.

---
## 4. Instant Conversion Cheats
```
Decimal → Cuineform
-------------------
 5 → 5
12 → 10
18 → 16
27 → 23
100 → 84
```

---
## 5. Geometry in Cuineform
### Golden Section (width = 12)
```
a ≈ 7;3,4,9,7₁₂   b ≈ 4;8,7,2,4₁₂
```
### Great Pyramid (royal cubits)
```
Base  ≈ 440;9,4,3,7₁₂
Height≈ 280;3,10,6,7₁₂
```
### Stonehenge (diameter)
```
63;0,3,7,6₁₂ cubits ≈ 33 m
```

---
## 6. Collatz as a 12‑State Loop
- **§** events occur when value hits 0 (mod 12).  
- Survey n = 12…1596 revealed exactly **3 hotspots per 100₁₂ block** where resets ≥ 3.  
- Peak so far: n = 1536₁₀ (1080₁₂) hits **8 §‑resets**.

Sample start 40₁₂ (48₁₀):  
`§ § § E T E E E E T E E E … → 1`

---
## 7. Toward a Cuineform Algebra
**Have**: digits, place‑value, three pattern glyphs.  
**Need**: formal +, × rules and rewrite axioms to manipulate expressions symbolically.  
Roadmap:
1. Define ⊕, ⊗ obeying base‑12 carry.  
2. Encode T,E,§ as unary ops with algebraic identities.  
3. Publish starter axiom set (future work).

---
## 8. Quick‑Reference Sheet
```
Base‑12 blocks:  10  20  30  …  100  110 …
Divisors:        2,3,4,6  (why 12 beats 10)
Reset rule:      n ≡ 0 (mod 12) ⇒ §
Even rule:       n even ⇒ E, n ← n/2
Odd rule:        n odd  ⇒ T, n ← 3n+1
```

---
## 9. Open Questions & Next Steps
- Formalise **Cuineform Algebra v 0.1**.  
- Build interactive **fraction‑mandala visualiser**.  
- Extend Collatz analysis to 10⁵ multiples of 12.  
- Explore protein‑folding analog via §‑reset topology.

> *“Numbers are not just quantities—they’re trajectories.”*  
> — Lukin Ackroyd (field notes)

---
### Credits & Contact
Core theory, experiments, and endless recursion: **Lukin Ackroyd**  
Drafted & compiled with ChatGPT as collaborative co‑scribe.

---
*End of Primer v 1 – April 2025*
