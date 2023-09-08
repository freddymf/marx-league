# Generated by Django 4.2.4 on 2023-09-08 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0003_team_grade_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='grade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='No Name', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='futbol.team'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='hc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hc_schedule', to='futbol.team'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='vs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vs_schedule', to='futbol.team'),
        ),
    ]