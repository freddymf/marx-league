from django.db import models
from .league import League


# Teams
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    description = models.CharField(max_length=300, null=True, blank=True)
    league = models.ManyToManyField(League)
    grade = models.CharField(max_length=50, null=True, blank=True)
    abbrev = models.CharField(max_length=3, null=True, blank=True)
    imagen = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name
