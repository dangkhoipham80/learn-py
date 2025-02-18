from zombie import *
from ogre import *

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
