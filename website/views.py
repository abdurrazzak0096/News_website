from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Category, FlashNews, SliderNews, LatestNews, Article, Video, LatestVideo, \
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
                messages.error(request,"User not found!!")
        else:
            messages.error(request, "User or Password Not Match!!")
        context = {'form':form}
        return render(request, 'login.html', context=context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login')

