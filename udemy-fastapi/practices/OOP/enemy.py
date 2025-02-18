class Enemy:

    def __init__(self, type_of_enemy = "Unknown", health_points = 10, attack_damage = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        print(f'New enemy created: {self.get_type_of_enemy()}')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a(n) {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you')

    def attack(self, e):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')
        e.health_points -= self.attack_damage  # Fix the typo (healths_point -> health_points)

    def special_attack(self):
        print("Enemy has no special attack!")