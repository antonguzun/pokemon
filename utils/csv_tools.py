import csv
from typing import Callable, Tuple

from utils.constraints import constraint_pokemon_effects, constraint_pokemon_types


class BaseCSVReader:
    filepath = None
    ignore_first_row = True
    constraints = None

    def __init__(self, filepath: str, constraints: Tuple[Callable] = None):
        self.filepath = filepath
        self.constraint_fun = constraints or self.constraints

    def apply_constraints(self, row: list):
        for constraint_fun in self.constraints:
            row = constraint_fun(row)
        return row

    def reader_gen(self):
        with open(self.filepath, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in enumerate(reader, start=1):

                if self.ignore_first_row and row[0] == 1:
                    continue

                row = self.apply_constraints(row[1])

                if row is None:
                    continue

                yield row


class PokemonCSVReader(BaseCSVReader):
    ignore_first_row = True
    constraints = (constraint_pokemon_types, constraint_pokemon_effects)
