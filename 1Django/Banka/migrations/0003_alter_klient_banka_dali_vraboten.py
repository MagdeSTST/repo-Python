# Generated by Django 4.2.2 on 2023-06-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banka', '0002_rename_vraboten_von_klient_banka_vraboten_vo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient_banka',
            name='dali_vraboten',
            field=models.BooleanField(default=1),
        ),
    ]