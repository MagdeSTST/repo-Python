from django.contrib import admin

from .models import Lice
from .models import Post
from .models import Klient
from .models import Naracka
from .models import Film

class NarackaInline(admin.StackedInline):
    model = Naracka


class  KlientAdmin(admin.ModelAdmin):
    list_display = ["ime","prezime","email","telefonski_broj","adresa_na_ziveenje"]
    inlines = [NarackaInline]

class  NarackaAdmin(admin.ModelAdmin):
    list_display = ["datum_na_narachka","suma_na_narachka","plateno"]

class  LiceAdmin(admin.ModelAdmin):

    def godina_na_raganje(self, Lice):
        return 2023 - Lice.godini
    
    list_display = ["ime" , "prezime", "email" , "grad" ,"godini", "godina_na_raganje"]


class  PostAdmin(admin.ModelAdmin):

    list_display = ["title" , "created_ad", "update_ad" ]
    list_filter = ["created_ad"]


class FilmAdmin(admin.ModelAdmin):

    list_display = ["ime", "zanr", "godina", "vremetranje_minuti", "dali_ima_nagrade"]

admin.site.register(Lice, LiceAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Klient,KlientAdmin)
admin.site.register(Naracka,NarackaAdmin)
admin.site.register(Film,FilmAdmin)

# Register your models here.
