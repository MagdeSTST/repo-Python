from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Tabela Lice(ime,prezime,email,godini,matichen broj,grad)

class Lice(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=100)
    ##email = models.EmailField()
    email = models.CharField(max_length=50, blank = True)
    godini = models.IntegerField(default=0)
    matichen_broj = models.CharField(max_length=13, unique= True)
    grad = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Klient(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=100)
    email = models.EmailField()
    telefonski_broj = models.CharField(max_length=30)
    adresa_na_ziveenje = models.CharField(max_length=100)

    def __str__(self):
        return self.ime

class Naracka(models.Model):
    suma_na_narachka = models.IntegerField()
    datum_na_narachka = models.DateTimeField(auto_now_add=True)
    plateno = models.BooleanField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
