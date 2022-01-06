import game_constants
import hero_data
import phase.phase_constants as phase_constants
from fight.battle import battle
from item.items import item_check, loose_items_after_lost_battle
from phase.abilities import abilities_update
from phase.check import phase_check, battle_check
from phase.intro import intro_phase
from phase.name import name_phase
from phase.start import start_game

current_phase = phase_constants.START

continue_game = True
while continue_game:
    if current_phase == phase_constants.START:
        current_phase = start_game()
    elif current_phase == phase_constants.INTRO:
        current_phase = intro_phase()
    elif current_phase == phase_constants.END:
        print(game_constants.DIVIDER)
        print("Dovidenia")
        continue_game = False
    elif current_phase == phase_constants.NAME:
        print(game_constants.DIVIDER)
        current_phase = name_phase()
    elif current_phase == phase_constants.INTRO_ABILITIES:
        print(game_constants.DIVIDER)
        abilities_update(game_constants.INTRO_ABILITIES_COUNT)
        print(game_constants.DIVIDER)
        current_phase = phase_check(phase_constants.FIGHT)
    elif current_phase == phase_constants.FIGHT:
        print(game_constants.DIVIDER)
        is_boss_fight = hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL
        win, health_remaining = battle(hero_data.fight_level)
        if win:
            if is_boss_fight:
                current_phase = phase_constants.WON_GAME
                continue

            print("Po vitaznej bitke ti ostal život " + str(health_remaining) + "/" + str(
                hero_data.abilities["Život"]["points"]))
            print("Po pridávaní bodov a voľby predmetu si budeš môcť doplniť život.")

            item_check(hero_data.fight_level)

            print(game_constants.DIVIDER)
            print("Po tvojej " + str(hero_data.fight_level) + ". výhre, ti pridávam " + str(
                hero_data.fight_level) + " body, ktoré môžeš využiť na upravenie tvojho hrdinu.")
            abilities_update(hero_data.fight_level)

            hero_data.fight_level += 1
            if hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL:
                print("Tvoj ďalší súper bude tvoj posledný a zároveň najsilnejší")
            print(game_constants.DIVIDER)
        else:
            loose_items_after_lost_battle()
            print("Potrebuješ si oddýchnuť a možno aj prehodnotiť svoje schopnosti, máš 0 života")
            print(game_constants.DIVIDER)

        max_health = hero_data.abilities["Život"]["points"]
        hero_data.abilities["Život"]["points"] = health_remaining
        current_phase = battle_check(hero_data.fight_level, max_health)

    elif current_phase == phase_constants.WON_GAME:
        print(game_constants.DIVIDER)
        print("\nPORAZIL SI POSLEDNÉHO SÚPERA. PREŠIEL SI CELÚ HRU. GRATULUJEM!!!")
        break
