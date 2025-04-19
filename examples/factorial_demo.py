"""
Demonstrates generating a sequence (factorials) entirely in base-12.
"""

from base12math import mul12, to_base12, from_base12 # Import from_base12 for verification

def factorial12(n: int) -> str:
    """Calculates the factorial of n entirely in base-12.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n as a base-12 string.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return "1" # 0! = 1

    result = "1"
    for i in range(2, n + 1):
        current_num_b12 = to_base12(i)
        result = mul12(result, current_num_b12)
    return result

def run_factorial_demo():
    """Runs the factorial demonstration."""
    print("--- Factorial Sequence Demo (Base-12) ---")

    for i in range(7): # Calculate up to 6!
        fact_b12 = factorial12(i)
        fact_dec = from_base12(fact_b12)
        print(f"{i}! = {fact_b12:<5} (Decimal: {fact_dec})")

if __name__ == "__main__":
    run_factorial_demo()
