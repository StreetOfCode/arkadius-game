import random
import time

import game_constants
from enemy_data import enemies
from hero_data import abilities


# (sila, sila + Obratnosť + skill)
def calculate_hero_attack():
    return (abilities["Útočná sila"]["points"],
            abilities["Útočná sila"]["points"] + abilities["Obratnosť"]["points"] + abilities["Skill"]["points"])


# (sila, sila + Obratnosť + skill)
def calculate_enemy_attack(enemy_data):
    return (enemy_data["Útočná sila"],
            enemy_data["Útočná sila"] + enemy_data["Obratnosť"] + enemy_data["Skill"])


def print_hero_stats(hero):
    print("Tvoj hrdina ide do súboja pripravený nasledovne:")
    print("Útok: mininum - " + str(hero["attack"][0]) + ", maximum - " + str(hero["attack"][1]))
    print("Šanca na kritický útok - " + str(hero["critical_hit"]) + "%")
    print("Obrana: mininum - " + str(hero["defence"][0]) + ", maximum - " + str(hero["defence"][1]))
    print("Život - ", str(hero["health"]))


def print_enemy_stats(enemy):
    print("Oproti nemu stojí príšera " + enemy["name"] + " s nasledovnými schopnosťami: ")
    print("Útok: mininum - " + str(enemy["attack"][0]) + ", maximum - " + str(enemy["attack"][1]))
    print("Šanca na kritický útok - " + str(enemy["critical_hit"]) + "%")
    print("Obrana: mininum - " + str(enemy["defence"][0]) + ", maximum - " + str(enemy["defence"][1]))
    print("Život - ", str(enemy["health"]))


def is_critical_hit(chance):
    return random.randint(0, 100) < chance


def simulate_battle(hero, enemy):
    print_hero_stats(hero)
    print()
    time.sleep(1)
    print_enemy_stats(enemy)
    time.sleep(3)

    print(game_constants.DIVIDER)
    print("\nZAČÍNAME SÚBOJ. AKO PRVÝ ÚTOČIŠ TY.\n")

    hero_turn = True
    while True:
        if hero_turn:
            min_attack, max_attack = hero["attack"]
            attack = random.randint(min_attack, max_attack)
            if is_critical_hit(hero["critical_hit"]):
                attack *= 3
                print("ÚTOČIŠ KRITICKÝM ÚTOKOM")

            min_defence, max_defence = enemy["defence"]
            defence = random.randint(min_defence, max_defence)
            final_attack = max((attack - defence), 0)

            if final_attack > 0:
                print("Zaútočil si útočnou silou - ", final_attack)
                enemy["health"] -= final_attack

                if enemy["health"] > 0:
                    print(enemy["name"] + " po tvojom útoku stále žije. Súperov zvyšok života - ", enemy["health"])
                else:
                    time.sleep(1)
                    print("ZVÍŤAZIL SI!\n")
                    print(game_constants.DIVIDER)
                    return True, hero["health"]
            else:
                print("Netrafil si...")

        else:
            min_attack, max_attack = enemy["attack"]
            attack = random.randint(min_attack, max_attack)
            if is_critical_hit(enemy["critical_hit"]):
                attack *= 3
                print("SÚPER ÚTOČÍ KRITICKÝM ÚTOKOM")

            min_defence, max_defence = hero["defence"]
            defence = random.randint(min_defence, max_defence)
            final_attack = max((attack - defence), 0)

            if final_attack > 0:
                hero["health"] -= final_attack
                print("Súper zaútočil útočnou silou - ", final_attack)

                if hero["health"] > 0:
                    print("Stále žiješ, zostáva ti " + str(hero["health"]) + " Života")
                else:
                    time.sleep(1)
                    print("PREHRAL SI\n")
                    print(game_constants.DIVIDER)
                    return False, 0
            else:
                print("Súperov útok ťa netrafil.")

        print()
        hero_turn = not hero_turn
        time.sleep(1)


def battle(fight_level):
    enemy_data = enemies[fight_level]

    hero = {
        "attack": calculate_hero_attack(),
        "critical_hit": min(100, (abilities["Skill"]["points"] * abilities["Šťastie"]["points"]) // 2),
        "defence": (abilities["Obrana"]["points"], abilities["Obrana"]["points"] + abilities["Obratnosť"]["points"]),
        "health": abilities["Život"]["points"]
    }

    enemy = {
        "name": enemy_data["name"],
        "attack": calculate_enemy_attack(enemy_data),
        "critical_hit": min(100, (enemy_data["Skill"] * enemy_data["Šťastie"]) // 2),
        "defence": (enemy_data["Obrana"], enemy_data["Obrana"] + enemy_data["Obratnosť"]),
        "health": enemy_data["Život"]
    }

    return simulate_battle(hero, enemy)
