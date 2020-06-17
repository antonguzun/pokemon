from django.db import models


class TypePokemon(models.Model):
    type_name = models.CharField(max_length=16, unique=True)


class Pokemon(models.Model):
    name = models.CharField(max_length=64)
    type_1 = models.ForeignKey(
        TypePokemon, related_name="firsts", on_delete=models.CASCADE, null=True
    )
    type_2 = models.ForeignKey(
        TypePokemon, related_name="secondaries", on_delete=models.CASCADE, null=True
    )

    hp = models.SmallIntegerField(null=False)
    attack = models.SmallIntegerField(null=False)
    defense = models.SmallIntegerField(null=False)
    spell_attack = models.SmallIntegerField(null=False)
    spell_defense = models.SmallIntegerField(null=False)
    speed = models.SmallIntegerField(null=False)

    generation = models.SmallIntegerField(default=1)

    @property
    def total(self):
        return (
            self.hp
            + self.attack
            + self.defense
            + self.spell_attack
            + self.spell_defense
            + self.speed
        )
