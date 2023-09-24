from django.contrib import admin

from website.models import Category, FlashNews, SliderNews, LatestNews, Article, Video, LatestVideo, SportLight, Tag, \
    Comment, Contact, WebsiteSetting, Art, ArtLatestNews, Magazine, AboutUs

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
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(WebsiteSetting)
admin.site.register(Art)
admin.site.register(ArtLatestNews)
admin.site.register(Magazine)
admin.site.register(AboutUs)
