import time

import enemy_data
import game_constants
import hero_data
import phase.phase_constants as phase_constants
from hero_update import hero_update
from save_load import save_game
from utility import print_abilities_points


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


def hero_check():
    print()
    print(hero_data.hero_name + ", Tvoje schopnosti sú momentálne na tom takto:")
    print_abilities_points()

    print("Máš " + str(hero_data.available_points) + " bodov na pridelenie schopností.")
    print()

    while True:
        print("0 - Späť")
        print("1 - Upraviť schopnosti hrdiny")

        choice = input("Čo chceš robiť? ")
        if choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "0":
            print()
            break
        elif choice == "1":
            hero_update()


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
            hero_check()
        elif choice == "2":
            save_game(next_phase)
        elif choice == "3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue


def rest_text(max_health):
    hero_current_life = hero_data.abilities["Život"]["points"]
    if hero_current_life < max_health:
        text = "Obnoviť 20 života. Do plného života ti chýba " + str(max_health - hero_current_life) + " bodov"
    else:
        text = "Máš síce plný život, ale oddych nikdy nie je zlý"

    return text


def battle_check(fight_level, max_health):
    enemy_name = enemy_data.enemies[fight_level]["name"]
    if fight_level == game_constants.BOSS_FIGHT_LEVEL:
        fight_against_text = "Posledný súboj. " + enemy_name
    else:
        fight_against_text = enemy_name

    while True:
        print("0 - Oddýchnuť si - " + rest_text(max_health))
        print("1 - Bojovať proti - " + fight_against_text)
        print("2 - Upraviť hrdinu")
        print("3 - Uložiť hru")
        print("4 - Ukončiť hru")
        choice = input("Aký je tvoj ďalsí krok?: ")
        if choice not in ["0", "1", "2", "3", "4"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "0":
            if hero_data.abilities["Život"]["points"] < max_health:
                print("Dobrá voľba, oddýchni si")
                time.sleep(2)
                hero_data.abilities["Život"]["points"] = min(hero_data.abilities["Život"]["points"] + 20, max_health)
                print("Tvoj život je teraz na tom takto: " + str(hero_data.abilities["Život"]["points"]) + "/" + str(
                    max_health))
                print()
            else:
                print("Uz mas plny Život")
                print()
        elif choice == "1":
            return phase_constants.FIGHT
        elif choice == "2":
            hero_check()
        elif choice == "3":
            save_game(phase_constants.FIGHT, fight_level)
        elif choice == "4":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue
