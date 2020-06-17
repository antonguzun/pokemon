from settings.base import PROJECT_ROOT


test_pokemons_csv_path = f"{PROJECT_ROOT}/tests/fixtures/test_pokemon.csv"

test_pokemons_ref = [
    [1, "TestPokemon1", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
    [2, "TestPokemon2", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, True],
    [3, "TestPokemon3", "Ghost", "Poison", 999, 99, 99, 99, 80, 80, 60, 1, False],
    [4, "TestPokemon4", "Steel", "Poison", 405, 100, 62, 63, 80, 80, 60, 1, False],
    [5, "TestPokemon5", "Fire", "Poison", 405, 10, 100, 63, 80, 80, 60, 1, False],
    [6, "TestPokemon6", "Bug", "Flying", 405, 10, 100, 63, 80, 80, 60, 1, False],
    [7, "TestPokemon7", "Bug", "Poison", 405, 10, 100, 63, 80, 80, 60, 1, False],
    [8, "TestPokemon8", "Steel", "Flying", 405, 10, 100, 63, 80, 80, 60, 1, False],
    [9, "G", "Steel", "Poison", 405, 10, 1, 63, 80, 80, 60, 1, False],
    [10, "Gamer", "Steel", "Poison", 405, 10, 1, 63, 80, 80, 60, 1, False],
    [11, "Gamer3000", "Fire", "Poison", 405, 10, 1, 63, 80, 80, 60, 1, False],
]

test_pokemons_with_effects_ref = [
    [1, "TestPokemon1", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
    [4, "TestPokemon4", "Steel", "Poison", 405, 200, 62, 63, 80, 80, 60, 1, False],
    [5, "TestPokemon5", "Fire", "Poison", 405, 10, 90.0, 63, 80, 80, 60, 1, False],
    [6, "TestPokemon6", "Bug", "Flying", 405, 10, 100, 63, 80, 80, 66.0, 1, False],
    [7, "TestPokemon7", "Bug", "Poison", 405, 10, 100, 63, 80, 80, 60, 1, False],
    [8, "TestPokemon8", "Steel", "Flying", 405, 20, 100, 63, 80, 80, 60, 1, False],
    [9, "G", "Steel", "Poison", 405, 20, 1, 63, 80, 80, 60, 1, False],
    [10, "Gamer", "Steel", "Poison", 405, 20, 1, 63 + 20, 80, 80, 60, 1, False],
    [11, "Gamer3000", "Fire", "Poison", 405, 10, 0.9, 63 + 40, 80, 80, 60, 1, False],
]
