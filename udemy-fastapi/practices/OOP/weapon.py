import random

class Weapon:
    def __init__(self, weapon_type, attack_increase, defense_increase=0):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase
        self.defense_increase = defense_increase

    def __str__(self):
        return f"{self.weapon_type} (ATK +{self.attack_increase}, DEF +{self.defense_increase})"

# Define various weapons and armor
weapons_list = [
    Weapon("Sword", 5),
    Weapon("Bow", 4),
    Weapon("Gun", 8),
    Weapon("Axe", 6),
    Weapon("Dagger", 3),
    Weapon("Shield", 0, 5),
    Weapon("Armor", 0, 8)
]

def get_random_weapon():
    return random.choice(weapons_list)
