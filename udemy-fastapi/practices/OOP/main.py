from zombie import *
from ogre import *
from hero import *
import random

def battle(e1: Enemy, e2: Enemy):
    print("\n🔥🔥🔥 LET THE BATTLE BEGIN! 🔥🔥🔥\n")

    e1.talk()
    e2.talk()

    turn = 1
    while e1.health_points > 0 and e2.health_points > 0:
        print("\n" + "=" * 50)
        print(f"⚔️ Round {turn}: {e1.get_type_of_enemy()} vs {e2.get_type_of_enemy()} ⚔️")
        print("=" * 50)
        print(f"🛡️ {e1.get_type_of_enemy()} HP: {e1.health_points}")
        print(f"🛡️ {e2.get_type_of_enemy()} HP: {e2.health_points}")

        # e1 Attacks e2
        e1.attack(e2)
        if e2.health_points <= 0:
            print(f"🏆 {e1.get_type_of_enemy()} is victorious! 🏆")
            break

        # e2 Attacks e1
        e2.attack(e1)
        if e1.health_points <= 0:
            print(f"🏆 {e2.get_type_of_enemy()} is victorious! 🏆")
            break

        # Special Turn every 3 rounds
        if turn % 3 == 0:
            print("\n💥 SPECIAL TURN ACTIVATED! 💥\n")

            # e1 Special Attack
            e1.special_attack(e2)
            e1.walk_forward()
            e1.attack(e2)
            if e2.health_points <= 0:
                print(f"🏆 {e1.get_type_of_enemy()} is victorious! 🏆")
                break

            # e2 Special Attack
            e2.special_attack(e1)
            e2.walk_forward()
            e2.attack(e1)
            if e1.health_points <= 0:
                print(f"🏆 {e2.get_type_of_enemy()} is victorious! 🏆")
                break

        turn += 1  # Increment round count

    print("\n🎇🎇🎇 BATTLE HAS ENDED! 🎇🎇🎇\n")


# Setup Enemies
zombie = Zombie(random.randint(100, 200), random.randint(1, 5))
ogre = Ogre(random.randint(100, 200), random.randint(1, 5))

# Start Battle
battle(zombie, ogre)

def hero_battle(hero: Hero, enemy: Enemy):
    print("\n🔥🔥🔥 HERO vs ENEMY BATTLE BEGINS! 🔥🔥🔥\n")

    print(f"🦸‍♂️ {hero}")
    print(f"👹 {enemy.get_type_of_enemy()} (HP: {enemy.health_points}, ATK: {enemy.attack_damage})\n")

    turn = 1
    while hero.health_points > 0 and enemy.health_points > 0:
        print("\n" + "=" * 50)
        print(f"⚔️ Round {turn}: Hero vs {enemy.get_type_of_enemy()} ⚔️")
        print("=" * 50)
        print(f"🛡️ Hero HP: {hero.health_points}")
        print(f"🛡️ {enemy.get_type_of_enemy()} HP: {enemy.health_points}")

        # Enemy attacks first
        enemy.attack(hero)
        if hero.health_points <= 0:
            print(f"🏆 {enemy.get_type_of_enemy()} has defeated the Hero! 🏆")
            break

        # Hero attacks back
        hero.attack(enemy)
        if enemy.health_points <= 0:
            print(f"🏆 Hero has defeated {enemy.get_type_of_enemy()}! 🏆")
            break

        # Special Turn every 3 rounds
        if turn % 3 == 0:
            print("\n💥 SPECIAL TURN ACTIVATED! 💥")

            # Enemy's special attack
            enemy.special_attack(hero)
            if hero.health_points <= 0:
                print(f"🏆 {enemy.get_type_of_enemy()} wins the battle! 🏆")
                break

            # Hero counterattacks
            hero.attack(enemy)
            if enemy.health_points <= 0:
                print(f"🏆 Hero is victorious against {enemy.get_type_of_enemy()}! 🏆")
                break

        turn += 1

    print("\n🎇🎇🎇 BATTLE HAS ENDED! 🎇🎇🎇\n")


# Setup Hero and Enemy
hero = Hero(random.randint(60, 90), random.randint(5, 10))
hero_weapon = get_random_weapon()
hero.equip_weapon(hero_weapon)

enemy_type = random.choice([Zombie, Ogre])
enemy = enemy_type(random.randint(100, 200), random.randint(1, 5))
enemy_weapon = get_random_weapon()
enemy.weapon = enemy_weapon
enemy.attack_damage += enemy_weapon.attack_increase
enemy.defense = enemy_weapon.defense_increase  # If it's a shield or armor

# Start Battle
hero_battle(hero, enemy)