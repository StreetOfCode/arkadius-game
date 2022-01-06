import phase.phase_constants as phase_constants

INTRO_TEXT = "Práve si zapol hru Arkadius, v ktorej budeš bojovať proti príšerám a pri tom si zlepšovať svojho hrdinu. Si na to pripravený?" \
             "\n 0 - Nie, bojím sa. \n 1 - Áno, poďme na to."


def intro_phase():
    while True:
        print(INTRO_TEXT)
        intro_choice = input("Aká je tvoja voľba?: ")
        if intro_choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if intro_choice == "0":
            print("To ma mrzí. Dúfam, že prídeš aspoň neskôr.")
            return phase_constants.END

        print("Výborne, máš odvahu. To sa mi páči.")
        return phase_constants.NAME
