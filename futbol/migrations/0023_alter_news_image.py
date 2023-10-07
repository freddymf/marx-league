# Generated by Django 4.2.4 on 2023-10-07 15:52

from django.db import migrations, models
import futbol.models.news


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0022_news_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=futbol.models.news.image_upload_path),
        ),
    ]
