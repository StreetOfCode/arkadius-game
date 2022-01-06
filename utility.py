import game_constants
from hero_data import abilities


def print_abilities_descriptions():
    print(game_constants.DIVIDER)
    for k, v in abilities.items():
        print(k + " - " + str(v["description"]))
    print(game_constants.DIVIDER)


def print_abilities_options(with_help_option=False):
    if with_help_option:
        print("0 - Vysvetlivky - načo su dobré jednotlivé schopnosti?")

    for i, ability in enumerate(abilities.keys()):
        ability_option = str(i + 1) + ' - ' + ability
        if ability == "Život":
            ability_option += " " + "- jeden bod pridá 5 života"
        print(ability_option)


def print_abilities_points():
    for k, v in abilities.items():
        print(k + " - " + str(v["points"]), end=", ")
    print("\n")
