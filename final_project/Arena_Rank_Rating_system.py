import random
import time


# ============================================================
# WEAPON
# ============================================================

class Weapon:
    def __init__(self, name, damage, attack_speed, weapon_type):
        self.name = name
        self.damage = damage
        self.attack_speed = attack_speed
        self.weapon_type = weapon_type

    def show(self):
        return (
            f"{self.name} ({self.weapon_type}) | "
            f"Damage: {self.damage} | "
            f"Attack Speed: {self.attack_speed}"
        )


# ============================================================
# ARMOR
# ============================================================

class Armor:
    def __init__(self, name, defense, health_bonus, armor_type):
        self.name = name
        self.defense = defense
        self.health_bonus = health_bonus
        self.armor_type = armor_type

    def show(self):
        return (
            f"{self.name} ({self.armor_type}) | "
            f"Defense: {self.defense} | "
            f"HP Bonus: +{self.health_bonus}"
        )


# ============================================================
# PLAYER
# ============================================================

class Player:
    def __init__(self, player_id, username, level, player_class,
                 weapon, armor):
        self.__id = player_id
        self.__username = username
        self.__level = level
        self.__player_class = player_class
        self.__weapon = weapon
        self.__armor = armor

        # Health is based on level and class.
        self.__max_health = self.calculate_health()
        self.__health = self.__max_health

        self.__rating = 1000
        self.__wins = 0
        self.__losses = 0
        self.__history = []

    def calculate_health(self):
        base_health = 100 + (self.__level * 10)

        class_bonus = {
            "Warrior": 80,
            "Mage": 20,
            "Archer": 40,
        }

        return (
            base_health
            + class_bonus.get(self.__player_class, 0)
            + self.__armor.health_bonus
        )

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

    def get_class(self):
        return self.__player_class

    def get_weapon(self):
        return self.__weapon

    def get_armor(self):
        return self.__armor

    def get_rating(self):
        return self.__rating

    def get_health(self):
        return self.__health

    def get_max_health(self):
        return self.__max_health

    def get_rank(self):
        if self.__rating >= 2500:
            return "Diamond"
        elif self.__rating >= 2000:
            return "Platinum"
        elif self.__rating >= 1500:
            return "Gold"
        elif self.__rating >= 1000:
            return "Silver"
        return "Bronze"

    def get_attack_damage(self):
        class_bonus = {
            "Warrior": 5,
            "Mage": 7,
            "Archer": 13,
        }

        return self.__weapon.damage + class_bonus.get(
            self.__player_class, 0
        )

    def get_defense(self):
        class_bonus = {
            "Warrior": 10,
            "Mage": 7,
            "Archer": 5,
        }

        return self.__armor.defense + class_bonus.get(
            self.__player_class, 0
        )

    def take_damage(self, damage):
        real_damage = max(1, damage - self.get_defense())
        self.__health = max(0, self.__health - real_damage)
        return real_damage

    def reset_health(self):
        self.__health = self.__max_health

    def win(self):
        old_rating = self.__rating
        self.__rating += 25
        self.__wins += 1
        self.__history.append(
            (old_rating, self.__rating, "+25")
        )

    def lose(self):
        old_rating = self.__rating
        self.__rating = max(0, self.__rating - 25)
        self.__losses += 1
        self.__history.append(
            (old_rating, self.__rating, "-25")
        )

    def show(self):
        print(
            f"ID: {self.__id} | "
            f"{self.__username} | "
            f"Lv.{self.__level} | "
            f"{self.__player_class} | "
            f"HP: {self.__max_health} | "
            f"Rating: {self.__rating} | "
            f"Rank: {self.get_rank()}"
        )

        print(f"  Weapon : {self.__weapon.show()}")
        print(f"  Armor  : {self.__armor.show()}")

    def show_history(self):
        print(f"\nRating History - {self.__username}")

        if not self.__history:
            print("No rating history.")
            return

        for old, new, change in self.__history:
            print(f"{old} -> {new} ({change})")


# ============================================================
# PLAYER CLASSES
# ============================================================

class Warrior(Player):
    def attack_description(self):
        return "Warrior performs a powerful melee attack."


class Mage(Player):
    def attack_description(self):
        return "Mage casts a powerful magic attack."


class Archer(Player):
    def attack_description(self):
        return "Archer fires a precise ranged attack."


# ============================================================
# MATCH
# ============================================================

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round_number = 0

    def calculate_damage(self, attacker, defender):
        # Small random factor makes every automatic match different.
        random_bonus = random.randint(0, 10)

        damage = (
            attacker.get_attack_damage()
            + random_bonus
        )

        return defender.take_damage(damage)

    def play(self):
        print("\n================================")
        print("        AUTOMATIC MATCH")
        print("================================")
        print(
            f"{self.player1.get_username()} "
            f"vs "
            f"{self.player2.get_username()}"
        )

        print("\nStarting battle...")

        self.player1.reset_health()
        self.player2.reset_health()

        # Prevent an extremely long battle.
        max_rounds = 50

        while (
            self.player1.get_health() > 0
            and self.player2.get_health() > 0
            and self.round_number < max_rounds
        ):
            self.round_number += 1

            print(f"\nRound {self.round_number}")

            # Attack order is based on weapon attack speed.
            if (
                self.player1.get_weapon().attack_speed
                >= self.player2.get_weapon().attack_speed
            ):
                first = self.player1
                second = self.player2
            else:
                first = self.player2
                second = self.player1

            damage = self.calculate_damage(first, second)

            print(
                f"{first.get_username()} attacks "
                f"with {first.get_weapon().name} "
                f"for {damage} damage."
            )

            print(
                f"{second.get_username()} HP: "
                f"{second.get_health()}/"
                f"{second.get_max_health()}"
            )

            if second.get_health() <= 0:
                break

            damage = self.calculate_damage(second, first)

            print(
                f"{second.get_username()} attacks "
                f"with {second.get_weapon().name} "
                f"for {damage} damage."
            )

            print(
                f"{first.get_username()} HP: "
                f"{first.get_health()}/"
                f"{first.get_max_health()}"
            )

            # Tiny delay makes the CLI battle easier to follow.
            time.sleep(0.3)

        if self.player1.get_health() > 0:
            winner = self.player1
            loser = self.player2
        else:
            winner = self.player2
            loser = self.player1

        winner.win()
        loser.lose()

        print("\n================================")
        print("           MATCH RESULT")
        print("================================")
        print(f"Winner : {winner.get_username()}")
        print(f"Loser  : {loser.get_username()}")
        print(f"Rounds : {self.round_number}")

        print(
            f"\n{winner.get_username()} Rating: "
            f"{winner.get_rating()}"
        )
        print(
            f"Rank: {winner.get_rank()}"
        )

        print(
            f"{loser.get_username()} Rating: "
            f"{loser.get_rating()}"
        )
        print(
            f"Rank: {loser.get_rank()}"
        )


# ============================================================
# ARENA SYSTEM
# ============================================================

class ArenaSystem:
    def __init__(self):
        self.players = []
        self.next_id = 1

    def create_weapon(self, player_class):
        weapons = {
            "Warrior": Weapon(
                "Iron Sword", 35, 5, "Sword"
            ),
            "Mage": Weapon(
                "Arcane Staff", 42, 4, "Magic"
            ),
            "Archer": Weapon(
                "Hunter Bow", 30, 7, "Bow"
            ),
        }

        return weapons[player_class]

    def create_armor(self, player_class):
        armors = {
            "Warrior": Armor(
                "Heavy Plate", 25, 100, "Heavy"
            ),
            "Mage": Armor(
                "Mystic Robe", 10, 40, "Light"
            ),
            "Archer": Armor(
                "Leather Armor", 15, 60, "Medium"
            ),
        }

        return armors[player_class]

    def add_player(self):
        print("\n--- ADD PLAYER ---")

        username = input("Username: ").strip()

        # New players automatically start at level 1.
        level = 1

        print("\n1. Warrior")
        print("2. Mage")
        print("3. Archer")

        choice = input("Class: ")

        class_data = {
            "1": ("Warrior", Warrior),
            "2": ("Mage", Mage),
            "3": ("Archer", Archer),
        }

        if choice not in class_data:
            print("Invalid class.")
            return

        class_name, player_class = class_data[choice]

        weapon = self.create_weapon(class_name)
        armor = self.create_armor(class_name)

        player = player_class(
            self.next_id,
            username,
            level,
            class_name,
            weapon,
            armor
        )

        self.players.append(player)
        self.next_id += 1

        print("\nPlayer created successfully!")
        player.show()

    def find_player(self, player_id):
        for player in self.players:
            if player.get_id() == player_id:
                return player

        return None

    def show_players(self):
        print("\n--- PLAYERS ---")

        if not self.players:
            print("No players.")
            return

        for player in self.players:
            player.show()
            print("-" * 60)

    def play_match(self):
        if len(self.players) < 2:
            print("You need at least 2 players.")
            return

        self.show_players()

        try:
            id1 = int(input("Player 1 ID: "))
            id2 = int(input("Player 2 ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        player1 = self.find_player(id1)
        player2 = self.find_player(id2)

        if not player1 or not player2:
            print("Player not found.")
            return

        if player1 == player2:
            print("A player cannot fight themselves.")
            return

        match = Match(player1, player2)
        match.play()

    def leaderboard(self):
        print("\n--- LEADERBOARD ---")

        if not self.players:
            print("No players.")
            return

        ranked_players = sorted(
            self.players,
            key=lambda player: player.get_rating(),
            reverse=True
        )

        for position, player in enumerate(
            ranked_players, 1
        ):
            print(
                f"{position}. "
                f"{player.get_username()} | "
                f"Rating: {player.get_rating()} | "
                f"Rank: {player.get_rank()}"
            )

    def rating_history(self):
        try:
            player_id = int(input("Player ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        player = self.find_player(player_id)

        if player:
            player.show_history()
        else:
            print("Player not found.")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    arena = ArenaSystem()

    # Preloaded first 5 players
    default_players = [
        ("Missfortune", 1, "Archer"),
        ("Gankplank", 1, "Warrior"),
        ("Tha", 1, "Mage"),
        ("Yantogaming", 1, "Archer"),
        ("sepiroth", 1, "Warrior"),
    ]

    player_classes = {
        "Warrior": Warrior,
        "Mage": Mage,
        "Archer": Archer,
    }

    for username, level, class_name in default_players:
        weapon = arena.create_weapon(class_name)
        armor = arena.create_armor(class_name)
        player = player_classes[class_name](
            arena.next_id,
            username,
            level,
            class_name,
            weapon,
            armor
        )
        arena.players.append(player)
        arena.next_id += 1

    while True:
        print("\n================================")
        print("       RANK ARENA MMORPG")
        print("================================")
        print("1. Add Player")
        print("2. Show Players")
        print("3. Play Automatic Match")
        print("4. Leaderboard")
        print("5. Rating History")
        print("6. Exit")

        choice = input("Choose menu: ")

        if choice == "1":
            arena.add_player()

        elif choice == "2":
            arena.show_players()

        elif choice == "3":
            arena.play_match()

        elif choice == "4":
            arena.leaderboard()

        elif choice == "5":
            arena.rating_history()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid menu.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()
