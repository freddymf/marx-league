# Generated by Django 4.2.4 on 2023-09-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0008_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='teams_logo/'),
        ),
    ]
