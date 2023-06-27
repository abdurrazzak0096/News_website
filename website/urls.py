
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/details/<int:article_id>', views.ArticleDetailView.as_view(), name='news-details'),
    path('news/comments/<int:article_id>', views.CommentView.as_view(), name='news-comments'),
    path('news/contact-us/', views.ContactView.as_view(), name='contact-us'),
    path('about-us/', views.AboutView.as_view(), name='about-us'),
    path('art/', views.art, name='art-page'),
    path('art/details/<int:artnews_id>', views.ArtDetailView.as_view(), name='art-news-details'),
    path('spotlight/details/<int:spotlight_id>', views.SpotLightDetailView.as_view(), name='spotlight-news-details'),

]