# Generated by Django 4.2.4 on 2023-10-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0020_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]
