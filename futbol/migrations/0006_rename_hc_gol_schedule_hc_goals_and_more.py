# Generated by Django 4.2.4 on 2023-09-12 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0005_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='hc_gol',
            new_name='hc_goals',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='vs_gol',
            new_name='vs_goals',
        ),
    ]
