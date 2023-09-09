from django.contrib import admin

from common.models import Player, Team, Schedule


# Register your models here.

# admin.site.register(Team)
# admin.site.register(Player)

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "grade"]
    inlines = [PlayerInline]


admin.site.register(Team, TeamAdmin)


class Scheduledmin(admin.ModelAdmin):
    list_display = ["stages", "hc", "hc_gol", "status", "vs_gol", "vs", "date" ]

admin.site.register(Schedule, Scheduledmin)