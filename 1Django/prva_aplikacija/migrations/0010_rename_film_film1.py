# Generated by Django 4.2.2 on 2023-07-03 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prva_aplikacija', '0009_rename_film1_film'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Film',
            new_name='Film1',
        ),
    ]