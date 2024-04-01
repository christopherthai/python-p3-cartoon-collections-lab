def roll_call_dwarves(dwarf_list):
    for i in range(len(dwarf_list)):
        print(f"{i+1}. {dwarf_list[i]}")


def summon_captain_planet(planeteer_calls):
    for i in range(len(planeteer_calls)):
        planeteer_calls[i] = planeteer_calls[i].capitalize() + "!"
    return planeteer_calls


def long_planeteer_calls(word):
    for i in range(len(word)):
        if len(word[i]) > 4:
            return True
    return False


def find_the_cheese(foods):
    for food in foods:
        if food in ["cheddar", "gouda", "camembert"]:
            return food
    return None
