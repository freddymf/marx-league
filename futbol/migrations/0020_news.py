# Generated by Django 4.2.4 on 2023-10-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0019_league_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
