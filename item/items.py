import hero_data
from item.item_data import items
from utility import print_items


def get_item_by_name(name):
    for items_in_level in items.values():
        for item in items_in_level.values():
            if item["name"] == name:
                return item
    return None


def loose_items_after_lost_battle():
    items_to_remove = []
    for item in hero_data.hero_items:
        if item["destroy_when_lost"]:
            items_to_remove.append(item)

    if len(items_to_remove) > 0:
        for to_remove in items_to_remove:
            remove_item(to_remove)
        print("Po prehranej bitke sa ti vymazali nasledujúce predmety:")
        for item_to_remove in items_to_remove:
            print(item_to_remove["name"], end=", ")
        print()


def replaces_item(chosen_item):
    if chosen_item["replaceable"]:
        tag = chosen_item["tag"]
        for hero_item in hero_data.hero_items:
            if hero_item["replaceable"] and hero_item["tag"] == tag:
                return hero_item
    return None


def remove_item(item):
    abilities_to_remove = item["ability"]
    for ability_key, ability_value in abilities_to_remove.items():
        hero_data.abilities[ability_key]["points"] -= ability_value
    hero_data.hero_items.remove(item)


def add_item(item):
    abilities_to_add = item["ability"]
    for ability_key, ability_value in abilities_to_add.items():
        if ability_value > 0:
            hero_data.abilities[ability_key]["points"] += ability_value
        else:
            hero_data.abilities[ability_key]["points"] = max(0,
                                                             hero_data.abilities[ability_key]["points"] - ability_value)

    hero_data.hero_items.append(item)


def item_check(level):
    available_new_items = items[level]
    print("\nPo výhre máš na výber z " + str(len(available_new_items)) + " predmetov")
    new_items_keys = list(available_new_items.keys())

    should_continue = True
    while should_continue:
        for item_key, item_value in available_new_items.items():
            print(str(item_key) + " - " + item_value["name"] + " -> " + item_value["description"])

        choice = input("Čo si vyberáš?: ")
        if not choice.isnumeric() or int(choice) not in new_items_keys:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue

        chosen_item = available_new_items[int(choice)]
        item_to_replace = replaces_item(chosen_item)
        if item_to_replace is not None:
            print(
                "Vybral si si " + chosen_item["name"] + " . Budeš musieť odhodiť predmet - " + item_to_replace["name"])

            confirmation = False
            while True:
                print("0 - Ok, potvrdzujem")
                print("1 - Nie, chcem niečo iné")
                replace_choice = input("Aká je tvoja voľba?: ")
                if replace_choice not in ["0", "1"]:
                    print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
                    continue

                if replace_choice == "0":
                    confirmation = True
                    break
                if replace_choice == "1":
                    break

            if confirmation:
                remove_item(item_to_replace)
                add_item(chosen_item)
                should_continue = False
            else:
                print("Opakujem výber predmetov")
                continue
        else:
            add_item(chosen_item)
            should_continue = False

    print("\nTvoje predmety sa aktualizovali. Teraz vyzerajú takto.")
    print_items()
