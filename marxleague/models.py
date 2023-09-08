from django.db import models

class Team(models.Model):
    def __init__(self, team_name):
        self.team_name = team_name

class Player(models.Model):
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

class Result(models.Model):
    def __init__(self, vs_team, hc_team, date):
        self.vs_team = vs_team
        self.hc_team = hc_team
        self.date = date