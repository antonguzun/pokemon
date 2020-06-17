def constraint_pokemon(self, row: list) -> [list, None]:
    if row[12]:
        return None
    if "Ghost" in row[2:4]:
        return None
    if "Steel" in row[2:4]:
        row[5] = row[5] * 2
    if "Fire" in row[2:4]:
        row[6] = row[6] * 0.9
    if "Bug" in row[2:4] and "Flying" in row[2:4]:
        row[10] = row[10] * 1.1
    if row[1][0] == "G":
        row[7] = row[7] + 5 * (len(row[1]) - 1)
    return row
