from django.contrib import admin

from futbol.models import Player, Schedule, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Schedule)
