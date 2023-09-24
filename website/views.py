from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Category, FlashNews, SliderNews, LatestNews, Article, Video, LatestVideo, \
    SportLight, Comment, WebsiteSetting, Art, ArtLatestNews, Magazine


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['slider_news'] = SliderNews.objects.last()
        context['latest_news'] = LatestNews.objects.all()[:3]
        context['categories'] = Category.objects.filter(is_active=True)
        context['articles'] = Article.objects.filter(is_draft=False)
        context['videos'] = Video.objects.all()
        context['latest_videos'] = LatestVideo.objects.filter(is_active=True)
        context['sport_lights'] = SportLight.objects.filter(is_active=True)
        context['sport_lights_middles'] = SportLight.objects.filter(is_active=False)
        context['sport_lights_display_right'] = SportLight.objects.filter(is_display_right=True)
        context['celebrity_news'] = SportLight.objects.filter(is_celebrity_news=True)
        context['website_settings'] = WebsiteSetting.objects.first()

        return context


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'news-details.html', context=context)


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = forms.RegisterForms(request.POST)

        if form.is_valid():
            password = form.data['password']
            user = form.save()
            user.set_password(password)
            user.save()
            # messages.success(request,"SignUP Success!! Please Go Back to Login Page")
            return redirect('/')

        context = {'form': form}
        return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = forms.LoginForms(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('/')
            except ObjectDoesNotExist:
                messages.error(request, "User not found!!")
        else:
            messages.error(request, "User or Password Not Match!!")
        context = {'form': form}
        return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login')


class CommentView(View):
    def post(self, request, article_id):
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.data['comment']
            Comment.objects.create(

                user=self.request.user,
                article_id=article_id,
                comment=comment

            ).save()
        else:
            messages.error(request, "Invalid Data Make Sure You Are OK")
        return redirect(f"/news/details/{article_id}")


class ContactView(View):
    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message was sent!")
        else:
            messages.error(request, "Invalid Data.")
        return redirect('/news/contact-us')

    def get(self, request):
        return render(request, 'contact-us.html')


class AboutView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = {
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'website_settings': WebsiteSetting.objects.first(),
        }
        return context


def art(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'website_settings': WebsiteSetting.objects.first(),
        'art_obj_mainCont': Art.objects.all(),
        'art_obj_latestNews': ArtLatestNews.objects.filter(is_trending_news=False),
        'art_obj_trendingNews': ArtLatestNews.objects.filter(is_trending_news=True)
    }
    return render(request, 'art.html', context)

class ArtDetailView(View):
    def get(self, request, artnews_id):
        artnews = Art.objects.get(id=artnews_id)
        context = {
            'news': artnews,
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'website_settings': WebsiteSetting.objects.first(),
            'flash_news': FlashNews.objects.last(),
            'latest_news': LatestNews.objects.all(),
        }
        return render(request, 'category_news_details.html', context=context)

class SpotLightDetailView(View):
    def get(self,request,spotlight_id):
        spotlightNews = SportLight.objects.get(id=spotlight_id)
        context = {
            'news': spotlightNews,
            'art_obj_latestNews' : LatestNews.objects.all(),
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'website_settings': WebsiteSetting.objects.first(),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'category_news_details.html', context=context)

# magazine section start
def magazine(request):
    context = {
        'menus': Category.objects.filter(is_menu=True, is_active=True),
        'website_settings': WebsiteSetting.objects.first(),
        'magazine_obj_mainCont': Magazine.objects.filter(is_trending_news=False,is_latest_news=False),
        'magazine_obj_latestNews': Magazine.objects.filter(is_latest_news=True),
        'magazine_obj_trendingNews': Magazine.objects.filter(is_trending_news=True)
    }
    return render(request, 'magazine.html', context)
class MagazineDetailView(View):
    def get(self, request, magazinenews_id):
        magazine_news = Magazine.objects.get(id=magazinenews_id)
        context = {
            'news': magazine_news,
            'latest_news': LatestNews.objects.all(),
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'website_settings': WebsiteSetting.objects.first(),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'category_news_details.html', context=context)

# magazine section end
# latestnews section start
class LatestNewsDetailView(View):
    def get(self, request, latestnews_id):
        magazine_news = LatestNews.objects.get(id=latestnews_id)
        context = {
            'news': magazine_news,
            'latest_news': LatestNews.objects.all(),
            'menus': Category.objects.filter(is_menu=True, is_active=True),
            'website_settings': WebsiteSetting.objects.first(),
            'flash_news': FlashNews.objects.last()
        }
        return render(request, 'category_news_details.html', context=context)

# latestnews section end