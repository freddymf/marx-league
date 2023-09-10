from django.urls import path

from futbol.views.pages.schedule_page_view import SchedulePageView
from futbol.views.pages.standings_page_view import  StandingsPageView
from futbol.views.pages.stats_page_view import StatsPageView
from .views.pages.landing_page_view import LandingPageView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing_page"),

    # path("standings/",  views.ScheduleView.as_view(), name="schedule_index")),
    path("schedule/", SchedulePageView.as_view(), name="schedule_page"),
    path("standings/", StandingsPageView.as_view(), name="standings_page"),
    path("stats/", StatsPageView.as_view(), name="stats_page"),
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