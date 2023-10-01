from django.db import models

from .player import Player
from .team import Team
from .league import League

class PlayerLeagueTeam(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} - {self.league.name} - {self.team.name}"