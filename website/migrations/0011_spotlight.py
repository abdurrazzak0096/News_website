# Generated by Django 4.2.1 on 2023-05-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_latestvideo_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotLight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='spotlights/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author_name', models.CharField(max_length=30)),
                ('author_image', models.ImageField(upload_to='authorImages/')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
