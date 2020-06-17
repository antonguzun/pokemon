from django.db import migrations
from utils.csv_tools import PokemonCSVReader
from settings.base import PROJECT_ROOT


def fill_data(apps, schema_editor):
    TypePokemon = apps.get_model("pokemon", "TypePokemon")
    Pokemon = apps.get_model("pokemon", "Pokemon")

    csv_reader = PokemonCSVReader(filepath=f"{PROJECT_ROOT}/fixtures/pokemon.csv")

    for row in csv_reader.reader_gen():

        type_1 = TypePokemon.objects.get_or_create(type_name=row[2])[0]
        type_2 = TypePokemon.objects.get_or_create(type_name=row[3])[0]

        Pokemon.objects.create(
            name=row[1],
            type_1=type_1,
            type_2=type_2,
            hp=row[5],
            attack=row[6],
            defense=row[7],
            spell_attack=row[8],
            spell_defense=row[9],
            speed=row[10],
            generation=row[11],
        )


class Migration(migrations.Migration):
    dependencies = [("pokemon", "0001_initial")]

    operations = [
        migrations.RunPython(fill_data, migrations.RunPython.noop, elidable=True)
    ]
