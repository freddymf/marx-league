from django.db import models
from .team import Team

# PLayers
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    grade = models.CharField(max_length=50, null=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
