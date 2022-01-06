import hero_data
import phase.phase_constants as phase_constants


def name_phase():
    while True:
        name = input("Ako sa bude volať tvoj hrdina?: ")
        print("Si si istý, ze sa tvoj hrdina bude volať " + name + "?")
        print("0 - Nie, chcem zmeniť meno\n1 - Áno")

        choice = input("Aká je tvoja voľba?: ")
        if choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "1":
            hero_data.hero_name = name
            return phase_constants.INTRO_ABILITIES
