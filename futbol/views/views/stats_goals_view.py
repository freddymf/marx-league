from datetime import date
from django.views.generic import TemplateView
from django.db.models import Q
from futbol.models.goal import Goal
from django.db.models import Sum, Case, When, IntegerField, Count

class StatsGoalsView(TemplateView):
    template_name = "views/stats_goals_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        goals = Goal.objects.values('player', 'player__name', 'player__team__name', 'player__imagen', 'player__team__imagen').annotate(
            goals=Count('player'),
            penalties=Sum(Case(When(penalty=True, then=1), default=0, output_field=IntegerField()))
        ).order_by('-goals')
        
        # if 'limit' in kwargs:  # limit
        #     goals = goals[:kwargs['limit']]

        context['goals'] = goals

        return context
