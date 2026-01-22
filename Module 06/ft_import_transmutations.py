import alchemy
from alchemy.elements import create_water

print("=== Import Transmutation Mastery ===")
print()

print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print()

print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}")

print("Method 3 - Aliased import")