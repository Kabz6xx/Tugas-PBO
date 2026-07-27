class Enemy:
    def __init__(self):
        print("Enemy dibuat")

    def attack(self):
        print("Enemy menyerang")


class FlyingEnemy(Enemy):
    def __init__(self):
        super().__init__()
        print("FlyingEnemy dibuat")

    def attack(self):
        super().attack()
        print("Menyerang dari udara")


class MagicEnemy(Enemy):
    def __init__(self):
        super().__init__()
        print("MagicEnemy dibuat")

    def attack(self):
        super().attack()
        print("Mengeluarkan serangan sihir")


class DragonBoss(FlyingEnemy, MagicEnemy):
    def __init__(self):
        super().__init__()
        print("DragonBoss dibuat")

    def attack(self):
        super().attack()
        print("Mengeluarkan Dragon Breath")


# Membuat objek boss
boss = DragonBoss()

print("\nAksi Serangan:")
boss.attack()
