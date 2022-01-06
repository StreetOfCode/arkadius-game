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
