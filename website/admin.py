from django.contrib import admin

from website.models import Category, FlashNews, SliderNews, LatestNews, Article, Video, LatestVideo, SportLight, Tag

# Register your models here.

admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(SliderNews)
admin.site.register(LatestNews)
admin.site.register(Article)
admin.site.register(Video)
admin.site.register(LatestVideo)
admin.site.register(SportLight)
admin.site.register(Tag)
