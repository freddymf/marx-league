from django.db import models


from .team import Team
from .league import League


# PLayers
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    grade = models.CharField(max_length=50, null=True, blank=True)

    imagen = models.CharField(max_length=100, null=True, blank=True)
    alias = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
