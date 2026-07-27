# Parent Class
class Weapon:
    def attack(self):
        print("attacking with weapon")  # Generic attack message

# Child Class 1
class Sword(Weapon):
    def attack(self):
        print("Sword: Slash Enemy with Sword!")

# Child Class 2
class Bow(Weapon):
    def attack(self):
        print("Bow: Shoot Enemy with an Arrow!")

# Child Class 3 (duck typing example)
class MagicStaff:
    def attack(self):
        print("Magic Staff: Casting Magic Spell!")

# Custom exception class for invalid weapons
class InvalidWeaponError(Exception):
    """Raised when attempting to use a non-weapon."""
    pass

# Function to use a weapon (duck typing)
def use_weapon(obj):
    # If object has no 'attack' method, raise custom exception
    if not hasattr(obj, 'attack'):
        raise InvalidWeaponError(f"{obj} is not a weapon and cannot attack.")
    obj.attack()

# Create weapon objects
sword = Sword()
bow = Bow()
staff = MagicStaff()

# Use each weapon inside a try/except/finally
try:
    use_weapon(sword)
except InvalidWeaponError as e:
    print(f"Error: {e}")
finally:
    print("Finished using sword.\n")

try:
    use_weapon(bow)
except InvalidWeaponError as e:
    print(f"Error: {e}")
finally:
    print("Finished using bow.\n")

try:
    use_weapon(staff)
except InvalidWeaponError as e:
    print(f"Error: {e}")
finally:
    print("Finished using staff.\n")

# Example with an invalid object
invalid_obj = "not a weapon"
try:
    use_weapon(invalid_obj)
except InvalidWeaponError as e:
    print(f"Caught an error: {e}")
finally:
    print("Finished attempting with invalid object.\n")
