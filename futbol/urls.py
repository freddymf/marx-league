from django.urls import path
from futbol.views.pages.league_page import LeaguePageView
from futbol.views.pages.news_detail import NewsDetailView
from futbol.views.pages.regulation_page import RegulationPageView

from futbol.views.pages.schedule_menu_option_page import ScheduleMenuOptionPageView
from futbol.views.pages.standings_menu_option_page import  StandingsMenuOptionPageView
from futbol.views.pages.stats_menu_option_page import StatsMenuOptionPageView
from futbol.views.pages.team_details_page import TeamDetailsPageView
from futbol.views.pages.teams_page import TeamsPageView
from .views.pages.home_page import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="landing_page"),
    path("regulation/", RegulationPageView.as_view(), name="regulation_page"),

    path("league/<slug:league_slug>/", LeaguePageView.as_view(), name="league_page"),

    path("teams/<slug:league_slug>/", TeamsPageView.as_view(), name="teams_page"),

    path("schedule/<str:league_slug>/", ScheduleMenuOptionPageView.as_view(), name="schedule_page"),
    path("standings/", StandingsMenuOptionPageView.as_view(), name="standings_page"),
    path("stats/<slug:league_slug>", StatsMenuOptionPageView.as_view(), name="stats_page"),
    path("team-details/<slug:league_slug>/<slug:team_slug>", TeamDetailsPageView.as_view(), name="team_details_page"),
   
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
 ]

