# Generated by Django 4.2.2 on 2023-06-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banka', '0003_alter_klient_banka_dali_vraboten'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Klient_Banka',
            new_name='Klient',
        ),
    ]