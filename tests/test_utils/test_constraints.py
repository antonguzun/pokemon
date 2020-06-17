import pytest

from utils.constraints import constraint_pokemon_types, constraint_pokemon_effects, fix_types


class TestPokemonConstraints:
    @pytest.fixture(autouse=True)
    def set_up(self):
        pass

    def test_fix_types(self):
        row = ["1", "34", "54.3", "test", "False", "True", "test_again"]
        types = (int, int, float, str, bool, bool, str)
        ref_row = [1, 34, 54.3, "test", False, True, "test_again"]
        assert fix_types(row, types) == ref_row

    def test_constraint_pokemon_types(self):
        row = ["1", "TestPokemon1", "Grass", "Poison", "318", "45", "49", "49", "65", "65", "45", "1", "False"]
        ref_row = [1, "TestPokemon1", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False]
        assert constraint_pokemon_types(row) == ref_row

    def test_constraint_pokemon_effects_legendary_and_ghosts(self):
        dirty_rows = [
            [1, "TestPokemon1", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, True],
            [2, "TestPokemon2", "Ghost", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, True],
            [3, "TestPokemon3", "Ghost", "Poison", 999, 99, 99, 99, 80, 80, 60, 1, False],
            [4, "TestPokemon4", "Rock", "Poison", 405, 100, 62, 63, 80, 80, 60, 1, False],
        ]
        rows = []
        for row in dirty_rows:
            result_row = constraint_pokemon_effects(row)
            if result_row:
                rows.append(result_row)
        assert len(rows) == 1
        assert rows == [[4, "TestPokemon4", "Rock", "Poison", 405, 100, 62, 63, 80, 80, 60, 1, False],]

    def test_constraint_pokemon_effects_steel(self):
        dirty_rows = [
            [3, "TestPokemon3", "Steel", "Poison", 999, 99, 99, 99, 80, 80, 60, 1, True],
            [4, "TestPokemon4", "Steel", "Poison", 405, 100, 62, 63, 80, 80, 60, 1, False],
        ]
        rows = []
        for row in dirty_rows:
            result_row = constraint_pokemon_effects(row)
            if result_row:
                rows.append(result_row)
        assert len(rows) == 1
        assert rows == [[4, "TestPokemon4", "Steel", "Poison", 405, 200, 62, 63, 80, 80, 60, 1, False],]

    def test_constraint_pokemon_effects_fire(self):
        dirty_rows = [
            [3, "TestPokemon3", "Fire", "Steel", 999, 99, 99, 99, 80, 80, 60, 1, True],
            [4, "TestPokemon4", "Fire", "Poison", 405, 100, 100, 63, 80, 80, 60, 1, False],
            [5, "TestPokemon5", "Fire", "Steel", 405, 100, 100, 63, 80, 80, 60, 1, False],
        ]
        rows = []
        for row in dirty_rows:
            result_row = constraint_pokemon_effects(row)
            if result_row:
                rows.append(result_row)
        assert len(rows) == 2
        assert rows == [
            [4, "TestPokemon4", "Fire", "Poison", 405, 100, 90.0, 63, 80, 80, 60, 1, False],
            [5, "TestPokemon5", "Fire", "Steel", 405, 200, 90.0, 63, 80, 80, 60, 1, False],
        ]

    def test_constraint_pokemon_effects_bug_and_flying(self):
        dirty_rows = [
            [2, "TestPokemon2", "Bug", "Flying", 405, 100, 100, 63, 80, 80, 60, 1, True],
            [3, "TestPokemon3", "Rock", "Flying", 999, 99, 99, 99, 80, 80, 60, 1, False],
            [4, "TestPokemon4", "Bug", "Poison", 405, 100, 100, 63, 80, 80, 60, 1, False],
            [5, "TestPokemon5", "Bug", "Flying", 405, 100, 100, 63, 80, 80, 60, 1, False],
        ]
        rows = []
        for row in dirty_rows:
            result_row = constraint_pokemon_effects(row)
            if result_row:
                rows.append(result_row)
        assert len(rows) == 3
        assert rows == [
            [3, "TestPokemon3", "Rock", "Flying", 999, 99, 99, 99, 80, 80, 60, 1, False],
            [4, "TestPokemon4", "Bug", "Poison", 405, 100, 100, 63, 80, 80, 60, 1, False],
            [5, "TestPokemon5", "Bug", "Flying", 405, 100, 100, 63, 80, 80, 66.0, 1, False],
        ]

    def test_constraint_pokemon_effects_gege(self):
        dirty_rows = [
            [4, "G", "Bug", "Poison", 405, 100, 100, 1, 80, 80, 60, 1, False],
            [5, "Gorrila30'@destroer", "Steel", "Flying", 405, 100, 100, 1, 80, 80, 60, 1, False],
        ]
        rows = []
        for row in dirty_rows:
            result_row = constraint_pokemon_effects(row)
            if result_row:
                rows.append(result_row)
        assert len(rows) == 2
        assert rows == [
            [4, "G", "Bug", "Poison", 405, 100, 100, 1, 80, 80, 60, 1, False],
            [5, "Gorrila30'@destroer", "Steel", "Flying", 405, 200, 100, 91, 80, 80, 60, 1, False],
        ]