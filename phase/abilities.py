import hero_data
from utility import print_abilities_points, print_abilities_options


def abilities_update():
    print(hero_data.hero_name + ", Tvoje schopnosti sú momentálne na tom takto:")
    print_abilities_points()
    print("Máš " + str(
        7) + " bodov, ktore si rozdeľ naprieč schopnostiam podla svojich preferencií.")

    abilities_picked = False
    abilities_picked_count = 0
    while not abilities_picked:
        print_abilities_options()
        option = input(
            "Máš " + str(
                7 - abilities_picked_count) + " možnosti na zlepšenie. Ktorú schopnosť chceš vylepšiť? ")
        if option.isnumeric() and int(option) in list(range(1, len(hero_data.abilities) + 1)):

            chosen_ability_name = list(hero_data.abilities.keys())[int(option) - 1]
            chosen_ability = hero_data.abilities[chosen_ability_name]
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
        "Výborne " + hero_data.hero_name + ". Dokončil si pridavánie schopnosti. Pre rekapituláciu, teraz vyzeraju tvoje schopnosti takto.")
    print_abilities_points()
