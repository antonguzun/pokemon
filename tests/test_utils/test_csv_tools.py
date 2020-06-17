import pytest

from tests.fixtures import (
    test_pokemons_csv_path,
    test_pokemons_ref,
    test_pokemons_with_effects_ref,
)
from utils.constraints import constraint_pokemon_types
from utils.csv_tools import PokemonCSVReader


class TestCSVTools:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.reader = PokemonCSVReader(test_pokemons_csv_path)

    def test_reader_without_constraint(self):
        self.reader.constraints = (constraint_pokemon_types,)
        rows_from_generator = []
        for row in self.reader.reader_gen():
            rows_from_generator.append(row)

        assert rows_from_generator == test_pokemons_ref

    def test_reader(self):
        rows_from_generator = []
        for row in self.reader.reader_gen():
            rows_from_generator.append(row)

        assert rows_from_generator == test_pokemons_with_effects_ref
