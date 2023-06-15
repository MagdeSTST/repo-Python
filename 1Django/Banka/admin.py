from django.contrib import admin

# Register your models here.
from .models import Klient
from .models import Transakciska_Smetka

class Transakciskaline(admin.StackedInline):
    model = Transakciska_Smetka


class  KlientAdmin(admin.ModelAdmin):
    list_display = ["ime","prezime","email","telefonski_broj","adresa_na_ziveenje"]
    inlines = [Transakciskaline]

class  Transakciska_SmetkaAdmin(admin.ModelAdmin):
    list_display = ["Klient_Banka","datum_na_kreiranje","sostojba","posledna_transakcija"]


admin.site.register(Klient, KlientAdmin)
admin.site.register(Transakciska_Smetka,Transakciska_SmetkaAdmin)