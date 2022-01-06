INTRO_TEXT = "Práve si zapol hru Arkadius, v ktorej budeš bojovať proti príšerám a pri tom si zlepšovať svojho hrdinu. Si na to pripravený?" \
             "\n 0 - Nie, bojím sa. \n 1 - Áno, poďme na to."

abilities = {
    "Útočná sila": {
        "points": 1,
        "description": "Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill."
    },
    "Obrana": {
        "points": 1,
        "description": "Celkový obrana sa ráta z bodov obrany + obratnosti."
    },
    "Obratnosť": {
        "points": 1,
        "description": "Obratnosť je dôležitá aj pre obranu aj pre útok."
    },
    "Skill": {
        "points": 1,
        "description": "SKill je dôležitý pri normálnom útoku ako aj kritickom útoku"
    },
    "Život": {
        "points": 50,
        "description": "Život je dôležitý pri bitke. Život sa dá doplniť po každom súboji."
    },
    "Šťastie": {
        "points": 1,
        "description": "Šťastie je dôležité pre kritický útok"
    }
}


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


continue_game = True
while continue_game:

    # intro
    print(INTRO_TEXT)
    intro_choice = input("Aká je tvoja voľba?: ")
    if intro_choice not in ["0", "1"]:
        print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
        continue

    if intro_choice == "0":
        print("To ma mrzí. Dúfam, že prídeš aspoň neskôr.")
        break

    print("Výborne, máš odvahu. To sa mi páči.")

    # name
    name_picked = False
    hero_name = ""
    while not name_picked:
        name = input("Ako sa bude volať tvoj hrdina?: ")
        print("Si si istý, ze sa tvoj hrdina bude volať " + name + "?")
        print("0 - Nie, chcem zmeniť meno\n1 - Áno")

        name_choice = input("Aká je tvoja voľba?: ")
        if name_choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if name_choice == "1":
            hero_name = name
            break

    print("Ahoj", hero_name)

    # points
    print(hero_name + ", Tvoje schopnosti sú momentálne na tom takto:")
    print_abilities_points()
    print("Máš 7 bodov, ktore si rozdeľ naprieč schopnostiam podla svojich preferencií.")
    abilities_picked = False
    abilities_picked_count = 0
    while not abilities_picked:
        print_abilities_options()

        option = input(
            "Máš " + str(7 - abilities_picked_count) + " možnosti na zlepšenie. Ktorú schopnosť chceš vylepšiť?: ")

        if option.isnumeric() and int(option) in list(range(1, len(abilities) + 1)):
            chosen_ability_name = list(abilities.keys())[int(option) - 1]
            chosen_ability = abilities[chosen_ability_name]
            print("\nVybral si si schopnosť - " + chosen_ability_name + ". Pridávam ti bod.")
            if chosen_ability_name == 'Život':
                chosen_ability["points"] += 5
            else:
                chosen_ability["points"] += 1
            print("Teraz tvoje body vyzerajú takto: ")
            print_abilities_points()
        else:
            print("Netrafil si výber, musím sa ťa spýtať ešte raz. \n")
            continue

        abilities_picked_count += 1
        if abilities_picked_count == 7:
            abilities_picked = True

    print(
        "Výborne " + hero_name + ". Dokončil si pridavánie schopnosti. Pre rekapituláciu, teraz vyzeraju tvoje schopnosti takto.")
    print_abilities_points()

    print("Si pripravený na prvý súboj?")
