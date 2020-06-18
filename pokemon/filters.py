import django_filters

from pokemon.models import Pokemon


class PokemonFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="contains")

    hp_from = django_filters.NumberFilter(
        field_name="hp", lookup_expr="gte", label="HP grater"
    )
    hp_to = django_filters.NumberFilter(
        field_name="hp", lookup_expr="lte", label="HP less"
    )

    attack_from = django_filters.NumberFilter(
        field_name="attack", lookup_expr="gte", label="Attack grater"
    )
    attack_to = django_filters.NumberFilter(
        field_name="attack", lookup_expr="lte", label="Attack less"
    )

    defense_from = django_filters.NumberFilter(
        field_name="defense", lookup_expr="gte", label="Defense grater"
    )
    defense_to = django_filters.NumberFilter(
        field_name="defense", lookup_expr="lte", label="Defense less"
    )

    class Meta:
        model = Pokemon
        fields = [
            "hp",
            "attack",
            "defense",
        ]
