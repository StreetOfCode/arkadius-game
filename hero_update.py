import hero_data
from utility import print_abilities_options, print_abilities_points


def hero_subtract_points():
    while True:
        print("0 - Už nechcem odoberať body. (Spat)")
        print_abilities_options()
        choice = input("Ktorej schopnosti chceš odobrať bod?: ")
        if choice == "0":
            break

        if choice.isnumeric() and int(choice) in list(range(1, len(hero_data.abilities) + 1)):
            chosen_ability_name = list(hero_data.abilities.keys())[int(choice) - 1]
            chosen_ability = hero_data.abilities[chosen_ability_name]
            if chosen_ability["points"] < 1:
                print("Danej schopnosti uz nemozem odstrániť bod")
                break

            print("\nVybral si si schopnosť - " + chosen_ability_name + ". Odoberám ti bod.")

            hero_data.available_points += 1

            if chosen_ability_name == 'Život':
                chosen_ability["points"] -= 5
            else:
                chosen_ability["points"] -= 1
            print("Teraz tvoje body vyzerajú takto: ")
            print_abilities_points()
        else:
            print("Netrafil si výber, musím sa ťa spýtať ešte raz. \n")
            continue


def hero_add_points():
    while True:
        if hero_data.available_points < 1:
            print("Uz nemáš žiadne body, ktoré by si mohol pridať.")
            break

        print("Máš " + str(hero_data.available_points) + " bodov na pridanie")
        print("0 - Už nechcem pridať body. (Späť)")
        print_abilities_options()
        choice = input("Ktorej schopnosti chces pridať bod?: ")

        if choice == "0":
            break

        if choice.isnumeric() and int(choice) in list(range(1, len(hero_data.abilities) + 1)):
            chosen_ability_name = list(hero_data.abilities.keys())[int(choice) - 1]
            chosen_ability = hero_data.abilities[chosen_ability_name]

            print("\nVybral si si schopnost - " + chosen_ability_name + ". Pridávam ti bod.")
            if chosen_ability_name == 'Život':
                chosen_ability["points"] += 5
            else:
                chosen_ability["points"] += 1

            hero_data.available_points -= 1

            print("Teraz tvoje body c takto: ")
            print_abilities_points()
        else:
            print("Netrafil si výber, musim sa ta spýtať ešte raz. \n")
            continue


def hero_update():
    while True:
        print("0 - Späť")
        print("1 - Pridať body (máš " + str(hero_data.available_points) + " bodov na pridanie)")
        print("2 - Odstrániť body zo schopnosti")

        choice = input("Aká je tvoja voľba?: ")
        if choice not in ["0", "1", "2"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "0":
            print()
            break
        elif choice == "1":
            if hero_data.available_points > 0:
                hero_add_points()
            else:
                print("Nemáš žiadne body, ktoré by si mohol pridať.")
                continue
        elif choice == "2":
            hero_subtract_points()
