
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/details/<int:article_id>', views.ArticleDetailView.as_view(), name='news-details'),
    path('news/comments/<int:article_id>', views.CommentView.as_view(), name='news-comments'),
    path('news/contact-us/', views.ContactView.as_view(), name='contact-us'),
    path('about-us/', views.AboutView.as_view(), name='about-us'),

]