# Generated by Django 4.2.4 on 2023-09-13 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0007_alter_schedule_mvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='mvp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='futbol.player'),
        ),
    ]