from django.urls import path

from futbol.views.pages.schedule_menu_option_page import ScheduleMenuOptionPageView
from futbol.views.pages.standings_menu_option_page import  StandingsMenuOptionPageView
from futbol.views.pages.stats_menu_option_page import StatsMenuOptionPageView
from .views.pages.home_page import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="landing_page"),

    # path("standings/",  views.ScheduleView.as_view(), name="schedule_index")),
    path("schedule/", ScheduleMenuOptionPageView.as_view(), name="schedule_page"),
    path("standings/", StandingsMenuOptionPageView.as_view(), name="standings_page"),
    path("stats/", StatsMenuOptionPageView.as_view(), name="stats_page"),
    # path("stats/", include("stats.urls")),
 ]


# urlpatterns = [
#     path("", views.ScheduleView.as_view(), name="schedule_index"),
# ]  


# urlpatterns = [
#     path("", views.StandingView.as_view(), name='standings_index'),
# ]  

# urlpatterns = [
#     path("", stats_view.StatsView.as_view(), name="stats_index"),
# ]  