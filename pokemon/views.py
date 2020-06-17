from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import BaseFilterView


class PokemonApiView(BaseFilterView, ListView):
    pass