from django.urls import reverse

import pytest
import requests


pytestmark = pytest.mark.django_db


class TestPokemonAPIListView:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = reverse("pokemon:pokemon_api")

    def test_urls(self):
        assert self.url == "/pokemon/"

    def test_get(self):
        response = requests.get(self.url)
        assert response.status_code == 200
