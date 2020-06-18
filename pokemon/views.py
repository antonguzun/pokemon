from django_filters import rest_framework as filters
from rest_framework import generics

from pokemon.filters import PokemonFilterSet
from pokemon.models import Pokemon
from serializers import PokemonSerializer


class PokemonApiView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PokemonFilterSet
