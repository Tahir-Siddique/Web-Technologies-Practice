# Generated by Django 3.2.8 on 2021-11-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Airports',
            new_name='Airport',
        ),
    ]