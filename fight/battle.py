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


def simulate_battle(hero, enemy):
    print_hero_stats(hero)
    print()
    time.sleep(1)
    print_enemy_stats(enemy)
    time.sleep(3)

    print(game_constants.DIVIDER)
    print("\nZAČÍNAME SÚBOJ. AKO PRVÝ ÚTOČIŠ TY.\n")


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
