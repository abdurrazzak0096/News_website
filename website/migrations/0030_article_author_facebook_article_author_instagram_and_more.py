# Generated by Django 4.2.1 on 2023-09-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_latestvideo_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]