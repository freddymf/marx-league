from django.db import models



# Teams
class League(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    teams = models.ManyToManyField('Team', related_name='leagues')

    def __str__(self):
        return self.name
