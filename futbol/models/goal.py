from pyexpat import model
from django.db import models

from futbol.models.player import Player
from futbol.models.schedule import Schedule
from .league import League


# Goal
class Goal(models.Model):
    min = models.CharField(max_length=2, null=True, blank=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    penalty = models.BooleanField()
    definition_of_penalties = (
        models.BooleanField()
    )  # Se utiliza si los peniltis son marcados para la definicion del partido

    def __str__(self):
        return self.min
