from rest_framework.serializers import ModelSerializer

from pokemon.models import Pokemon, TypePokemon


class TypePokemonSerializer(ModelSerializer):
    class Meta:
        model = TypePokemon
        fields = ["type_name"]


class PokemonSerializer(ModelSerializer):
    type_1 = TypePokemonSerializer()
    type_2 = TypePokemonSerializer()

    class Meta:
        model = Pokemon
        fields = [
            "id",
            "name",
            "type_1",
            "type_2",
            "total",
            "hp",
            "attack",
            "defense",
            "spell_attack",
            "spell_defense",
            "speed",
            "generation",
        ]
