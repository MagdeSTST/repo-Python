# Generated by Django 4.2.2 on 2023-06-13 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prva_aplikacija', '0005_post_update_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefonski_broj', models.CharField(max_length=30)),
                ('adresa_na_ziveenje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Naracka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suma_na_narachka', models.IntegerField()),
                ('datum_na_narachka', models.DateTimeField(auto_now_add=True)),
                ('plateno', models.BooleanField()),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prva_aplikacija.klient')),
            ],
        ),
    ]