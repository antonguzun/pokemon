from django.urls import path
from pokemon.views import PokemonApiView

urlpatterns = [
    path("pokemon/", PokemonApiView.as_view(), name="pokemon_api"),
]
