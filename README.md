<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="lukinackc" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>

# base12math

**Duodecimal math via cuneiform operators**

A pure Python library for base-12 (“duodecimal”) arithmetic using digits `0–9, T, E`.

## Key Features

*   **Zero-dependency duodecimal arithmetic:** Perform calculations directly in base-12 without intermediate decimal conversion.
*   **Human-friendly digits:** Uses standard `0–9` plus `T` (10) and `E` (11).
*   **Native carry-aware algorithms:** Addition and multiplication handle arbitrary-length strings correctly.
*   **Composability:** Build higher-order functions (factorials, etc.) entirely in base-12.
*   **Compactness & divisibility:** Base-12’s factors (2, 3, 4, 6) can simplify representation.

## Installation

```sh
# Clone the repository (if you haven't already)
# git clone <your-repo-url>
# cd base12math

# Install the package
pip install .
```

## Usage Examples

See the `examples/` directory for runnable scripts (`convert_demo.py`, `arithmetic_demo.py`, `compose_demo.py`, `factorial_demo.py`).

### 1. Basic Conversion

```python
from base12math import to_base12, from_base12

# Decimal → Duodecimal
print(to_base12(0))      # "0"
print(to_base12(10))     # "T"   (10₁₀ → T₁₂)
print(to_base12(11))     # "E"   (11₁₀ → E₁₂)
print(to_base12(12))     # "10"  (12₁₀ → 10₁₂)
print(to_base12(143))    # "EE"  (11*12 + 11)

# Duodecimal → Decimal
print(from_base12("0"))  # 0
print(from_base12("T"))  # 10
print(from_base12("E"))  # 11
print(from_base12("10")) # 12
print(from_base12("EE")) # 143
```

### 2. Addition & Carrying

```python
from base12math import add12

# Simple sums (5 + 7 = 12₁₀ -> 10₁₂)
print(add12("5", "7"))     # "10"

# (125 + 59 = 184₁₀ -> 1*144 + 3*12 + 4 = 134₁₂)
print(add12("T5", "4E"))   # "134"

# Carry across multiple digits (1715 + 28 = 1743₁₀ -> 1*1728 + 0*144 + 1*12 + 3 = 1013₁₂)
print(add12("E8E", "24"))  # "1013"
```

### 3. Multiplication & Place Value

```python
from base12math import mul12

# (3 * 4 = 12₁₀ -> 10₁₂)
print(mul12("3", "4"))   # "10"

# (10 * 10 = 100₁₀ -> 8*12 + 4 = 84₁₂)
print(mul12("T", "T"))   # "84"

# (13 * 13 = 169₁₀ -> 1*144 + 2*12 + 1 = 121₁₂)
print(mul12("11", "11")) # "121"
```

### 4. Composing Operations

Chain operations without intermediate decimal conversion.

```python
from base12math import add12, mul12

# Compute (A + B) * C all in base‑12
A, B, C = "T3", "4E", "2"      # A=123, B=59, C=2 (decimal)
sum_ab = add12(A, B)           # 123 + 59 = 182₁₀ -> "132"₁₂
product = mul12(sum_ab, C)     # 182 * 2 = 364₁₀ -> "264"₁₂
print(f"({A} + {B}) * {C} = {product}") # Output: (T3 + 4E) * 2 = 264
```

### 5. Generating a Sequence (Factorials)

```python
from base12math import mul12, to_base12

def factorial12(n: int) -> str:
    if n < 0: raise ValueError("Negative input")
    if n == 0: return "1"
    result = "1"
    for i in range(2, n + 1):
        result = mul12(result, to_base12(i))
    return result

# 5! = 120₁₀ -> 10*12 + 0 = A0₁₂
print(factorial12(5))   # "A0"
# 6! = 720₁₀ -> 5*144 + 0*12 + 0 = 500₁₂
print(factorial12(6))   # "500"
