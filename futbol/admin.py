from django.contrib import admin

from .models.goal import Goal

from .models.league import League
from .models.player import Player
from .models.team import Team
from .models.schedule import Schedule


# Register your models here.

# admin.site.register(Team)
# admin.site.register(Player)


############################################################
# Teams and Players
############################################################


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "grade"]
    inlines = [PlayerInline]


admin.site.register(Team, TeamAdmin)

############################################################
# League and Teams
############################################################


class TeamInline(admin.TabularInline):
    model = Team.league.through
    extra = 0


class LeagueAdmin(admin.ModelAdmin):
    # list_display = ["name"]
    inlines = [TeamInline]


admin.site.register(League, LeagueAdmin)


############################################################
# League and Teams
############################################################


class GoalInline(admin.TabularInline):
    model = Goal
    extra = 0


class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "league",
        "date",
        "stages",
        "hc",
        "hc_goals",
        "status",
        "vs_goals",
        "vs",
        "hc_points",
        "vs_points",
        "hc_definition_penalties",
        "vs_definition_penalties",
        "mvp",
    ]
    inlines = [GoalInline]


admin.site.register(Schedule, ScheduleAdmin)

############################################################
# Goals
############################################################

admin.site.register(Goal)

# admin.site.register(Player)
