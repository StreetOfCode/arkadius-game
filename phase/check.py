import phase.phase_constants as phase_constants


def end_game_choice():
    print("Si si istý že chceš ukončiť hru?")
    while True:
        print("0 - Späť")
        print("1 - Áno, ukončiť.")

        choice = input("Naozaj ukonciť? ")
        if choice not in ["0", "1"]:
            print("Netrafil si, pýtam sa ešte raz")
            continue

        if choice == "0":
            return False
        elif choice == "1":
            return True


def phase_check(next_phase):
    while True:
        print("0 - Pokračovať na", next_phase)
        print("1 - Upraviť hrdinu")
        print("2 - Uložiť hru")
        print("3 - Ukončiť hru")
        choice = input("Aký je tvoj ďalší krok? ")
        if choice not in ["0", "1", "2", "3"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "0":
            return next_phase
        elif choice == "1":
            # TODO hero check
            continue
        elif choice == "2":
            # TODO save game
            continue
        elif choice == "3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue