# Generated by Django 4.2.4 on 2023-09-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0002_team_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='alias',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='imagen',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
