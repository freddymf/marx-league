from django.contrib import admin

from futbol.models import Player, Schedule, Team

# Register your models here.

# admin.site.register(Team)
# admin.site.register(Player)



class PlayerInline(admin.TabularInline):
    model = Player
    extra = 3


class TeamAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    # ]
    list_display = ["name", "grade"]
    inlines = [PlayerInline]


admin.site.register(Team, TeamAdmin)


class Scheduledmin(admin.ModelAdmin):
    list_display = ["stages", "hc", "hc_gol", "status", "vs_gol", "vs", "date" ]

admin.site.register(Schedule, Scheduledmin)