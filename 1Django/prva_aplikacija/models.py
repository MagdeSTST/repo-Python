from typing import Any
from django.db import models

# Create your models here.

#Tabela Lice(ime,prezime,email,godini,matichen broj,grad)

class Lice(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=100)
    email = models.EmailField
    godini = models.IntegerField
    matichen_broj = models.CharField(max_length=13)
    grad = models.CharField(max_length=50)