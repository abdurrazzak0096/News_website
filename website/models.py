from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    is_menu = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    file_path = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class FlashNews(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SliderNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider/')
    news_type = models.CharField(max_length=30, null=True, blank=True)
    news_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class LatestNews(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='latestNews/')
    timeStamp = models.TimeField(auto_now=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField()
    author_name = models.CharField(max_length=30)
    author_image = models.ImageField(upload_to='authorImages/')
    author_facebook = models.CharField(max_length=200,null=True,blank=True)
    author_youtube = models.CharField(max_length=200,null=True,blank=True)
    author_twitter = models.CharField(max_length=200,null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    is_draft = models.BooleanField(default=True)

    @property
    def get_short_desc(self):
        return self.description[0:120]

    def get_related_post(self):
        return Article.objects.filter(tags__in=self.tags.all())[:2]

    def __str__(self):
        return self.title

    def get_comment(self):
        return self.comment_set.all()


class Video(models.Model):
    video_url = models.CharField(max_length=200)
    video_type = models.CharField(max_length=30)
    video_thumbnail = models.ImageField(upload_to='videosThumbnails/', blank=True, null=True)

    def __str__(self):
        return self.video_type


class LatestVideo(models.Model):
    image = models.ImageField(upload_to='latestVideos/')
    title = models.CharField(max_length=150)
    video_url = models.CharField(max_length=200,null=True)
    is_active = models.BooleanField(default=True)


class SportLight(models.Model):
    banner = models.ImageField(upload_to='spotlights/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author_name = models.CharField(max_length=30)
    author_image = models.ImageField(upload_to='authorImages/')
    timeStamp = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    is_display_right = models.BooleanField(default=False)
    is_celebrity_news = models.BooleanField(default=False)

    @property
    def get_short_desc(self):
        return self.description[:100]

    def get_mini_desc_(self):
        return self.description[:50]

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.user_id}"


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


# start code for Art.html
class Art(models.Model):
    banner = models.ImageField(upload_to='Arts_image/')
    title = models.CharField(max_length=100)
    timeStamp = models.TimeField(auto_now=True)
    description = models.TextField()

    def get_short_desc(self):
        return self.description[:120]

    def __str__(self):
        return self.title


class ArtLatestNews(models.Model):
    banner = models.ImageField(upload_to='latest_news/')
    title = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now=True)
    is_trending_news = models.BooleanField(default=False)


# end code for Art.html


# start code for magazine.html
class Magazine(models.Model):
    banner = models.ImageField(upload_to='Magazine_image/')
    title = models.CharField(max_length=100)
    timeStamp = models.TimeField(auto_now=True)
    description = models.TextField()
    is_trending_news = models.BooleanField(default=False)
    is_latest_news = models.BooleanField(default=False)

    def get_short_desc(self):
        return self.description[:120]

    def __str__(self):
        return self.title
# end code for magazine.html

class AboutUs(models.Model):
    image = models.ImageField(upload_to='about_us/')
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()
    paragraph_three = models.TextField()
    paragraph_four = models.TextField()


class WebsiteSetting(models.Model):
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    facebook_link = models.CharField(max_length=250)
    twitter_link = models.CharField(max_length=250)
    youtube_link = models.CharField(max_length=250)
    copy_right = models.CharField(max_length=100,blank=True,null=True)
