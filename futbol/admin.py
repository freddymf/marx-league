from django.contrib import admin
from futbol.models.news import News

from futbol.models.player_league_team import PlayerLeagueTeam
from futbol.models.standing import Standing 

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


# class PlayerInline(admin.TabularInline):
#     model = Player
#     extra = 0


# class TeamAdmin(admin.ModelAdmin):
#     list_display = ["name", "grade"]
#     inlines = [PlayerInline]

class PlayerLeagueTeamInline(admin.TabularInline):
    model = PlayerLeagueTeam
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlayerLeagueTeamInline]

admin.site.register(Player, PlayerAdmin)



############################################################
# League and Teams
############################################################

class ReadOnlyTeamInline(admin.TabularInline):
    model = League.teams.through
    extra = 0
    can_delete = False
    verbose_name_plural = 'Teams'

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['team'].disabled = True
        return formset

class LeagueAdmin(admin.ModelAdmin):
    inlines = [ReadOnlyTeamInline]

admin.site.register(League, LeagueAdmin)
admin.site.register(Team)

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
        # "hc_points",
        # "vs_points",
        "hc_definition_penalties",
        "vs_definition_penalties",
        "mvp",
    ]
    inlines = [GoalInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
           
        try:
            # Save the original Schedule object
            original_schedule = Schedule.objects.get(pk=obj.pk)

            # Call the parent save_model method to save the updated Schedule
         

            # Check if any field in the Schedule model has changed
            # if original_schedule != obj:
                # Perform operations on other models (e.g., Stats)
                # Here, we'll update the Stats model when Schedule is updated
            Standing.update_stat_form_league(request, obj, form, change)
            
        except Schedule.DoesNotExist:
            original_schedule = None
            
    def delete_model(self, request, obj):
        # Perform any necessary actions before deleting the model
        # For example, you can log the deletion or perform related operations

        # Call the parent class method to delete the model
        super().delete_model(request, obj)
        # Perform any additional actions after deleting the model
        # For example, you can update related records or send notifications
        Standing.update_stat_form_league(request, obj, form=None, change=None)

        

            
            
        # Update de Stat table
        #stats = Stat.objects.first()
            # stats.updated = True
            # stats.save()

admin.site.register(Schedule, ScheduleAdmin)

############################################################
# Goals
############################################################

admin.site.register(Goal)


class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
    ]

admin.site.register(News, NewsAdmin)


class StandingAdmin(admin.ModelAdmin):
    list_display = [
        "league",
        "team",
        "pj",
        "pg",
        "pp",
        "pe",
        "pts",
    ]


admin.site.register(Standing, StandingAdmin)

