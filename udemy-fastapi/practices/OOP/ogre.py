from enemy import Enemy
import random

class Ogre(Enemy):  # Fixed spelling from "Orge" to "Ogre"

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):  # Method overriding
        print('*Gruhhh... Ogre is slamming hands all around!*')

    def attack(self, e):
        print(f'{self.get_type_of_enemy()} attacks {e.get_type_of_enemy()} for {self.attack_damage} damage')
        e.health_points -= self.attack_damage
        print(f'{e.get_type_of_enemy()} now has {e.health_points} HP')

    def special_attack(self, e):
        did_special_attack_work = random.random() < 0.2  # 20% chance
        if did_special_attack_work:
            self.health_points += 4
            print('Ogre regenerated 4 HP and dealt 3 bonus damage!')
            e.health_points -= 3
        else:
            print('Ogre tried to regenerate but failed!')