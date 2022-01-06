from hero_data import abilities


def print_abilities_options():
    for i, ability in enumerate(abilities.keys()):
        ability_option = str(i + 1) + ' - ' + ability
        if ability == "Život":
            ability_option += " " + "- jeden bod pridá 5 života"
        print(ability_option)


def print_abilities_points():
    for k, v in abilities.items():
        print(k + " - " + str(v["points"]), end=", ")
    print("\n")
