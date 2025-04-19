# examples/sequences_demo.py
"""
Demonstrates prime numbers and the Fibonacci sequence in base-12,
highlighting potential visual patterns.
"""

from base12math import to_base12
import math

# --- Helper Functions ---

def is_prime(n: int) -> bool:
    """Basic primality test."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Only need to check factors up to sqrt(n)
    # Check factors 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(count: int) -> list[int]:
    """Generates the first 'count' prime numbers."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(count: int) -> list[int]:
    """Generates the first 'count' Fibonacci numbers (starting with 0)."""
    fibs = []
    a, b = 0, 1
    for _ in range(count):
        fibs.append(a)
        a, b = b, a + b
    return fibs

# --- Main Demonstration ---

def run_sequences_demo():
    """Runs the prime and Fibonacci sequence demonstration."""
    print("--- Prime Numbers in Base-10 and Base-12 ---")
    num_primes = 25 # How many primes to generate
    primes_dec = generate_primes(num_primes)

    print("Decimal | Base-12")
    print("--------|---------")
    for p in primes_dec:
        p_b12 = to_base12(p)
        print(f"{p:<7} | {p_b12}")

    print("\nPattern Note:")
    print("In base-12, prime numbers greater than 3 must end in 1, 5, 7, or E.")
    print("This is because:")
    print(" - Ends in 0, 2, 4, 6, 8, T => Divisible by 2")
    print(" - Ends in 0, 3, 6, 9       => Divisible by 3")


    print("\n--- Fibonacci Sequence in Base-10 and Base-12 ---")
    num_fibs = 25 # How many Fibonacci numbers to generate
    fibs_dec = generate_fibonacci(num_fibs)

    print("n | Decimal   | Base-12")
    print("--|-----------|---------")
    for i, f in enumerate(fibs_dec):
        f_b12 = to_base12(f)
        print(f"{i:<2} | {f:<9} | {f_b12}")

    print("\nPattern Note:")
    print("Observe the repeating pattern of the last digit in the base-12 Fibonacci sequence:")
    last_digits = [to_base12(f)[-1] for f in fibs_dec if f > 0] # Exclude 0 for clarity
    print("Last digits:", " ".join(last_digits))
    print("(The sequence of last digits repeats every 24 terms: 1, 1, 2, 3, 5, 8, 1, 9, T, 7, 5, 0, 5, 5, T, 3, 1, 4, 5, 9, 2, E, 1, 0...)")


if __name__ == "__main__":
    run_sequences_demo()
