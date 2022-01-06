import game_constants
import phase.phase_constants as phase_constants
from phase.abilities import abilities_update
from phase.intro import intro_phase
from phase.name import name_phase

current_phase = phase_constants.INTRO

continue_game = True
while continue_game:

    if current_phase == phase_constants.INTRO:
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
        abilities_update()
        print(game_constants.DIVIDER)
        print("Si pripravený na prvý súboj?")
        break
