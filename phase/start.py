import hero_data
import phase.phase_constants as phase_constants
from phase.check import phase_check
from save_load import load_game


def start_game():
    while True:
        print("0 - Začať novú hru")
        print("1 - Načítať uloženú hru")

        choice = input("Aká je tvoja voľba?: ")
        if choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        if choice == "0":
            return phase_constants.INTRO
        elif choice == "1":
            result, load_phase = load_game()
            print("Hra sa načítala...Vitaj späť " + hero_data.hero_name)
            if result:
                return phase_check(load_phase)
