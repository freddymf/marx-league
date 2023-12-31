# Generated by Django 4.2.4 on 2023-09-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0012_player_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='league',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='leagues',
            field=models.ManyToManyField(to='futbol.league'),
        ),
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(to='futbol.team'),
        ),
    ]
