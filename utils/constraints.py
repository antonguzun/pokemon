from distutils.util import strtobool


def fix_types(row: list, types_list: tuple) -> list:
    for i in range(len(types_list)):
        if types_list[i] is bool:
            row[i] = bool(strtobool(row[i]))
        else:
            row[i] = types_list[i](row[i])
    return row


def constraint_pokemon_types(row: list) -> [list, None]:
    types = (
        int,
        str,
        str,
        str,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        bool,
    )
    return fix_types(row, types)


def constraint_pokemon_effects(row: list) -> [list, None]:
    if row[12] or "Ghost" in row[2:4]:  # exclude legendary and ghosts
        return None
    if "Steel" in row[2:4]:  # double hp
        row[5] = row[5] * 2
    if "Fire" in row[2:4]:  # lower attack
        row[6] = row[6] * 0.9
    if "Bug" in row[2:4] and "Flying" in row[2:4]:  # increase speed
        row[10] = row[10] * 1.1
    if row[1][0] == "G":  # increase defence
        row[7] = row[7] + 5 * (len(row[1]) - 1)
    return row
