# Generated by Django 4.2.2 on 2023-07-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prva_aplikacija', '0008_film1_delete_film'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Film1',
            new_name='Film',
        ),
    ]