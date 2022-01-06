from os import listdir
from os.path import isfile, join

import game_constants
import hero_data


def load(file_name):
    print("Načítavam hru uloženú pod názvom - " + file_name.replace(".txt", ""))
    with open("saved/" + file_name, encoding="utf-8") as f:
        name_loaded = False
        abilities_loaded = False
        abilities_loaded_count = 0
        next_phase = ""
        next_phase_loaded = False
        available_points_loaded = False

        for line in f:
            if not name_loaded:
                hero_data.hero_name = line.rstrip()
                name_loaded = True
            elif not abilities_loaded:
                ability_key, points = line.rstrip().split(" - ")
                hero_data.abilities[ability_key]["points"] = int(points)
                abilities_loaded_count += 1
                if abilities_loaded_count == len(hero_data.abilities):
                    abilities_loaded = True
            elif not next_phase_loaded:
                next_phase = line.rstrip()
                next_phase_loaded = True
            elif not available_points_loaded:
                hero_data.available_points = int(line.rstrip())
                available_points_loaded = True

        print()
        return True, next_phase


def load_game():
    print(game_constants.DIVIDER)
    saves = []
    for file in listdir("saved"):
        if isfile(join("saved", file)):
            saves.append(file)
    if len(saves) > 0:
        print("0 - Späť")
        for i, save in enumerate(saves):
            print(str(i + 1) + " - " + save.replace(".txt", ""))

        while True:
            choice = input("Ktorú hru chceš načítať? ")
            if choice == "0":
                print()
                return False, ""

            if not choice.isdigit() or int(choice) not in list(range(1, len(saves) + 1)):
                print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
                continue
            else:
                game_to_load = saves[int(choice) - 1]
                return load(game_to_load)

    else:
        print("Nemáš žiadne uložené hry")
        return False, ""


def save_game(next_phase):
    print("Pod akým názvom chceš uložiť hru? (Názov nesmie obsahovať čisla, špeciálne znaky ani medzery)")
    while True:
        save_name = input("Nazov - ")
        if save_name.isalpha():
            file_path = "saved/" + save_name + ".txt"
            file_handler = open(file_path, "w", encoding="utf-8")
            file_handler.write(hero_data.hero_name)
            file_handler.write("\n")
            for k, v in hero_data.abilities.items():
                file_handler.write(str(k) + ' - ' + str(v["points"]))
                file_handler.write("\n")
            file_handler.write(next_phase)
            file_handler.write("\n")
            file_handler.write(str(hero_data.available_points))
            file_handler.write("\n")
            file_handler.close()
            print("Úspešne som uložil hru")
            print()
            break
        else:
            print("Tvoj názov neobsahuje iba písmena. Skús ešte raz")
            continue
