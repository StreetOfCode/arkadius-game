import hero_data


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
            file_handler.close()
            print("Úspešne som uložil hru")
            print()
            break
        else:
            print("Tvoj názov neobsahuje iba písmena. Skús ešte raz")
            continue
