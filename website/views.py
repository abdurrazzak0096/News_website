from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from website.models import Category, FlashNews, SliderNews, LatestNews, Article, Video, LatestVideo,  \
    SportLight


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['slider_news'] = SliderNews.objects.last()
        context['latest_news'] = LatestNews.objects.all()
        context['categories'] = Category.objects.filter(is_active=True)
        context['articles'] = Article.objects.filter(is_draft=False)
        context['videos'] = Video.objects.all()
        context['latest_videos'] = LatestVideo.objects.filter(is_active=True)
        context['sport_lights'] = SportLight.objects.filter(is_active=True)
        context['sport_lights_middles'] = SportLight.objects.filter(is_active=False)
        context['sport_lights_display_right'] = SportLight.objects.filter(is_display_right=True)
        context['celebrity_news'] = SportLight.objects.filter(is_celebrity_news=True)

        return context

class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'news-details.html', context=context)


