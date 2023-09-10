from django.views.generic import TemplateView


class StatsPageView(TemplateView):
    template_name = "pages/stats_page.html"
