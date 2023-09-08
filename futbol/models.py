from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, default="No Name")
    grade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100, unique=True, default="No Name")
    grade = models.CharField(max_length=50, null=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('scheduled', 'Scheduled'),
        ('raining', 'Raining'),
        ('playing', 'Playing'),
        ('pending', 'Pending'),
    ]
      
    vs = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="vs_schedule", null=True
    )
    hc = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="hc_schedule", null=True
    )
    date = models.DateField(null=True)
    vs_gol = models.IntegerField(null=True)
    hc_gol = models.IntegerField(null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    
