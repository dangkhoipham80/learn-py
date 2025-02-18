from enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy = 'Zombie',
                         health_points = health_points,
                         attack_damage = attack_damage)

    def talk(self): # method overriding
        print(f'{self.get_type_of_enemy()} grumbles...')

    def spread_disease(self):
        print('The zombie is trying to spread infection')

    def special_attack(self, e):
        did_special_attack_work = random.random() < 0.5  # 50% chance
        if did_special_attack_work:
            self.health_points += 2
            e.health_points -= 5;
            print(f'{self.get_type_of_enemy()} regenerated 2 HP and dealt 5 bonus damage!!')
        else:
            print(f'{self.get_type_of_enemy()} tried to regenerate but failed!')