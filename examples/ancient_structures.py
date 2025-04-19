"""
Compare famous ancient structures in base-10 and Cuineform (base-12) numbers.
"""
from base12math import to_base12

def show_structure(name, base_cubits, height_cubits, unit="cubits"):
    print(f"{name}:")
    print(f"  Base:   {base_cubits} (base-10)  |  {to_base12(base_cubits)}₁₂ (Cuineform)")
    print(f"  Height: {height_cubits} (base-10)  |  {to_base12(height_cubits)}₁₂ (Cuineform)")
    ratio = base_cubits / height_cubits
    print(f"  Ratio (base/height): {ratio:.5f} (base-10)")
    print(f"  Ratio (Cuineform):   {to_base12(base_cubits)}/{to_base12(height_cubits)}")
    print()

if __name__ == "__main__":
    print("Ancient Structures: Base-10 vs. Cuineform (Base-12)\n")

    # Great Pyramid of Giza (approximate, in royal cubits)
    show_structure("Great Pyramid of Giza", base_cubits=440, height_cubits=280)

    # Stonehenge Sarsen Circle (diameter, in cubits)
    show_structure("Stonehenge Sarsen Circle", base_cubits=63, height_cubits=2)  # Height is arbitrary for circle

    # Parthenon (stylobate length/width, in feet)
    show_structure("Parthenon (Athens)", base_cubits=228, height_cubits=101, unit="feet")

    # Golden Rectangle (for reference)
    golden_a = 233
    golden_b = 144
    show_structure("Golden Rectangle", base_cubits=golden_a, height_cubits=golden_b, unit="units")

    print("Try plugging in your own measurements to see how they look in Cuineform!")
