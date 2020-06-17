from django.views.generic import ListView, View

from django_filters.views import BaseFilterView
from django.http import HttpResponse

# class PokemonApiView(BaseFilterView, ListView):
#     pass

class PokemonApiView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')



