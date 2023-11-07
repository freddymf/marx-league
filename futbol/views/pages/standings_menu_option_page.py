from django.views.generic import TemplateView

from futbol.models.league import League
from futbol.views.views.standing_view import StandingView
from django.template.loader import render_to_string

class StandingsMenuOptionPageView(TemplateView):
    template_name = "pages/standings_menu_option_page.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        league = League.objects.get(slug=self.kwargs.get('league_slug'))

        standing_view = StandingView(**kwargs)
        standing_context = standing_view.get_context_data(request=self.request, league_slug=self.kwargs.get('league_slug'))
        standing_view = render_to_string(standing_view.template_name, standing_context)

        context['standing_view'] = standing_view
        context['league'] = league

        return context