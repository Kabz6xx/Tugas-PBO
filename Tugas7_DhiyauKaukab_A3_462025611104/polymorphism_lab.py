# Parent Class
class Weapon:
    def attack(self):
        print("Senjata melakukan serangan")


# Child Class 1
class Sword(Weapon):
    def attack(self):
        print("Sword: Menebas musuh dengan pedang!")


# Child Class 2
class Bow(Weapon):
    def attack(self):
        print("Bow: Menembakkan panah ke musuh!")


# Child Class 3 (untuk menunjukkan Duck Typing)
class MagicStaff:
    def attack(self):
        print("Magic Staff: Mengeluarkan serangan sihir!")


# Fungsi Duck Typing
def use_weapon(obj):
    obj.attack()


# Membuat objek
sword = Sword()
bow = Bow()
staff = MagicStaff()

# Mengirim objek berbeda ke fungsi yang sama
use_weapon(sword)
use_weapon(bow)
use_weapon(staff)