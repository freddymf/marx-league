from django.views.generic import TemplateView
from futbol.views.views.stats_goals_view import StatsGoalsView
from django.template.loader import render_to_string


class StatsMenuOptionPageView(TemplateView):
    template_name = "pages/stats_menu_option_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stats_goals_view = StatsGoalsView(**kwargs)
        stats_goals_context = stats_goals_view.get_context_data(request=self.request, limits=5, show_details=True)
        stats_goals_view = render_to_string(stats_goals_view.template_name, stats_goals_context)

        context['stats_goals_view'] = stats_goals_view

        return context