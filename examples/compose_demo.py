"""
Demonstrates composing base-12 operations without intermediate decimal conversion.
"""

from base12math import add12, mul12, from_base12 # Import from_base12 for verification

def run_compose_demo():
    """Runs the composition demonstration."""
    print("--- Composing Operations Demo ---")

    # Compute (A + B) * C all in base‑12
    A, B, C = "T3", "4E", "2" # A=123, B=59, C=2

    print(f"A = {A} ({from_base12(A)}) ")
    print(f"B = {B} ({from_base12(B)}) ")
    print(f"C = {C} ({from_base12(C)}) ")

    sum_ab = add12(A, B)       # 123 + 59 = 182 -> 1*144 + 3*12 + 2 = 132 base-12
    print(f"A + B = {sum_ab} ({from_base12(sum_ab)}) ")

    product = mul12(sum_ab, C) # 182 * 2 = 364 -> 2*144 + 6*12 + 4 = 264 base-12
    print(f"({A} + {B}) * {C} = {product} ({from_base12(product)}) ")

if __name__ == "__main__":
    run_compose_demo()
