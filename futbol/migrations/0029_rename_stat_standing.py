# Generated by Django 4.2.4 on 2023-11-07 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0028_alter_schedule_hc_definition_penalties_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stat',
            new_name='Standing',
        ),
    ]