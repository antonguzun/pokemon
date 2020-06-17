import csv
from distutils.util import strtobool
from typing import Callable

from utils.pokemon_point_editor import constraint_pokemon


class BaseCSVReader:
    filepath = None
    ignore_first_row = True
    constraints_types = None
    constraint_fun = None

    def __init__(self, filepath: str, constraint_fun: Callable = None):
        self.filepath = filepath
        self.constraint_fun = constraint_fun or self.constraint_fun

    def fix_types(self, row: list) -> list:
        for i in range(len(self.constraints_types)):
            if self.constraints_types[i] is bool:
                row[i] = bool(strtobool(row[i]))
            else:
                row[i] = self.constraints_types[i](row[i])
        return row

    def reader_gen(self):
        with open(self.filepath, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in enumerate(reader, start=1):

                if self.ignore_first_row and row[0] == 1:
                    continue

                row = self.fix_types(row[1])
                row = self.constraint_fun(row) if self.constraint_fun else row
                if row is None:
                    continue
                yield row


class PokemonCSVReader(BaseCSVReader):
    ignore_first_row = True
    constraints_types = (
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
    constraint_fun = constraint_pokemon
