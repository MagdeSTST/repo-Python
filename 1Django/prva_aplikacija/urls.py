from django.urls import path
from .views import *


urlpatterns = [
    path('prva-funkcija/',hello_world), #http://127.0.0.1:8000/prva-funkcija/
    path('pecatenje-method/',pecatenje_metod),
    path('zbir-na-broevi/', zbir_na_broevi),
    path('sobiranje/', sobiranje),
    path('matematicki_operacii/',matematicki_operacii),


    path('prv_post_metod/',prv_post_metod),
    path('soberi_broevi_post/',soberi_broevi_post),

    ##Class Base
    path("prva_klasa/",prvaKlasaAPI.as_view()),
    path("checkGetOrPost/",checkGetOrPost.as_view()),
    path("lica/",LiceAPI.as_view()),
    path("licafilter/",LiceFilter.as_view())
   ## path("film/",FilmAPI.as_view())
]