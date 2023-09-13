from django.db import models
from .team import Team


# PLayers
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    grade = models.CharField(max_length=50, null=True, blank=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    imagen = models.CharField(max_length=3, null=True, blank=True)
    alias = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
