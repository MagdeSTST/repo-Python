from typing import Any, Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
    def save(self) -> None:
        print('Nov klient se ima dodadeno')
        print (self.ime)
        self.ime = self.ime.capitalize()
        print (self.ime)
        return super().save()

class Naracka(models.Model):
    suma_na_narachka = models.IntegerField()
    datum_na_narachka = models.DateTimeField(auto_now_add=True)
    plateno = models.BooleanField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)


@receiver(post_save, sender = Lice)
def lice_ps(sender, instance, created, **kwargs):
    if "@" in instance.email:
        print('Podatokot e email')
    else:
        print('Podatokot ne e email')

@receiver(post_save, sender = Lice)
def lice_ps(sender, instance, created, **kwargs):
    if created == True:
        if  instance.godini > 17 :
            print('Лицето е полнолетно')
        else:
            print('Лицето е малолетно')


@receiver(post_save, sender = Post)
def post_ps(sender, instance, created, **kwargs):
    if  len(instance.text) > 100:
        print(len(instance.text))
        print('Постот е поголем од 100 карактери')
    else:
        print('Постот е пократок од 100 карактери')