from django.db import models

# Create your models here.



class Klient(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=100)
    email = models.EmailField()
    telefonski_broj = models.CharField(max_length=30)
    adresa_na_ziveenje = models.CharField(max_length=100)
    dali_e_vraboten = models.BooleanField(default=1)
    vraboten_vo= models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.ime



class Transakciska_Smetka(models.Model):
    sostojba = models.CharField(max_length=50)
    datum_na_kreiranje =models.DateTimeField(auto_now_add=True)
    posledna_transakcija = models.DateTimeField(auto_now=True)
    Klient_Banka = models.ForeignKey(Klient, on_delete=models.CASCADE )
    
