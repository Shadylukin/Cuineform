"""
Pure base-12 (duodecimal) math utilities.

This module provides basic conversion and arithmetic functions for base-12 numbers
represented as strings using digits 0-9, T (10), and E (11).
"""

DIGITS = "0123456789TE"
DIGIT_MAP = {c: i for i, c in enumerate(DIGITS)}

def to_base12(n: int) -> str:
    """Convert a non-negative integer to its duodecimal string (digits 0–9,T,E).

    Args:
        n: A non-negative integer.

    Returns:
        The duodecimal string representation of n.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return "0"
    
    base12_str = []
    while n > 0:
        remainder = n % 12
        base12_str.append(DIGITS[remainder])
        n //= 12
    
    return "".join(reversed(base12_str))

def from_base12(s: str) -> int:
    """Parse a duodecimal string (digits 0–9,T,E) back to an integer.

    Args:
        s: The duodecimal string. Case-insensitive.

    Returns:
        The integer value represented by the string.

    Raises:
        ValueError: If the string is empty or contains invalid characters.
    """
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    
    s = s.strip().upper()
    decimal_value = 0
    power = 0
    
    for digit in reversed(s):
        if digit not in DIGIT_MAP:
            raise ValueError(f"Invalid duodecimal digit: '{digit}'")
        decimal_value += DIGIT_MAP[digit] * (12 ** power)
        power += 1
        
    return decimal_value

def add12(a: str, b: str) -> str:
    """Add two duodecimal strings, returning their sum as a duodecimal string.

    Args:
        a: The first duodecimal number string.
        b: The second duodecimal number string.

    Returns:
        The duodecimal string representing the sum of a and b.
    """
    num_a = from_base12(a)
    num_b = from_base12(b)
    sum_val = num_a + num_b
    return to_base12(sum_val)

def mul12(a: str, b: str) -> str:
    """Multiply two duodecimal strings, returning their product as a duodecimal string.

    Args:
        a: The first duodecimal number string.
        b: The second duodecimal number string.

    Returns:
        The duodecimal string representing the product of a and b.
    """
    num_a = from_base12(a)
    num_b = from_base12(b)
    product_val = num_a * num_b
    return to_base12(product_val)
