from django.db import models


class TypePokemon(models.Model):
    type_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.type_name


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

    def __str__(self):
        return f"{self.name}: {self.type_1} and {self.type_2} with total={self.total}"

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
