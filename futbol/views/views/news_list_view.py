from django.views.generic import TemplateView
from futbol.models.news import News

class NewsListView(TemplateView):
    # model = News
    template_name = 'views/news_list_view.html'
    # context_object_name = 'news_list'
    # paginate_by = 10  # Si deseas paginar los resultados

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = News.objects.all()

        context['news_list'] = news_list
        return context