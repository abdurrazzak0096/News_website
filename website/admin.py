from django.contrib import admin

from website.models import Category, FlashNews, SliderNews,LatestNews

# Register your models here.

admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(SliderNews)
admin.site.register(LatestNews)
