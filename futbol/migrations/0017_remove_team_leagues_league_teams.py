# Generated by Django 4.2.4 on 2023-09-30 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0016_team_leagues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='leagues',
        ),
        migrations.AddField(
            model_name='league',
            name='teams',
            field=models.ManyToManyField(related_name='leagues', to='futbol.team'),
        ),
    ]
