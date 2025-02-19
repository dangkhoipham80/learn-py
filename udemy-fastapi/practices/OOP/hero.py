from weapon import *

class Hero:
    def __init__(self, health_points, attack_damage, type_of_enemy = 'Hero'):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.type_of_enemy = 'Hero'
        self.weapon = None
        self.defense = 0  # Defense stat added

    def equip_weapon(self, weapon: Weapon):
        if self.weapon is None:
            self.weapon = weapon
            self.attack_damage += weapon.attack_increase
            self.defense += weapon.defense_increase
            print(f"⚔️ Hero equipped {weapon}!")

    def attack(self, enemy):
        damage = max(1, self.attack_damage - enemy.defense)
        print(f"💥 Hero attacks {enemy.get_type_of_enemy()} for {damage} damage!")
        enemy.health_points -= damage

    def __str__(self):
        return f"Hero (HP: {self.health_points}, ATK: {self.attack_damage}, DEF: {self.defense}, Weapon: {self.weapon})"
