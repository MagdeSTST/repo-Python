from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView ## ova ni treba za klasa

from .serializers import LiceSerializers##,FilmSerializers
from .models import Lice,Film

# Create your views here.
@api_view(['GET','POST'])
def hello_world(request): ##request e zadol]itelen parametar sto mora da se ispraka
    return Response({'response' : 'success'})


@api_view(['GET','POST'])
def pecatenje_metod(request):
    if request.method == 'GET':
        print('Методот е GET')
    elif request.method == 'POST':
        print('Методот е POST')
    return Response({'response' : 'success print'})

@api_view(["GET", "POST"])
def zbir_na_broevi(request):
    broevi = {
        'prv_broj': 2,
        'vtor_broj': 5
    }
    if request.method == "GET":
        broevi['zbir'] = broevi["prv_broj"] + broevi["vtor_broj"]
        print('Zbirot na vasite broevi e {}.'.format(broevi['zbir']))
        print('Metodot e GET')
    elif request.method == "POST":
        broevi['zbir'] = broevi["vtor_broj"] + broevi['vtor_broj']
        print('Zbirot na vasite broevi e {}.'.format(broevi["zbir"]))
        print('Metodot e POST')
    print(broevi)
    return Response(broevi)


@api_view(['GET'])
def sobiranje(request):
    print(request.GET)
    zbir = int(request.GET.get('broj1',0)) + int(request.GET.get('broj2',0))
    return Response({'response':zbir})


@api_view(["GET"])
def matematicki_operacii(request):
    data = {}
    data["broj1"] = int(request.GET.get("broj1", 0))
    data["broj2"] = int(request.GET.get("broj2", 0))

    data["operacija"] = request.GET.get("operacija")
    if data["operacija"] == "sobiranje":
        data["zbir"] = data['broj1']+data["broj2"]

    elif data["operacija"] == "odzemanje":
        data["razlika"] = data['broj1']-data["broj2"]

    elif data["operacija"] == "mnozenje":
            data["proizvod"] = data['broj1']*data["broj2"]

    elif data["operacija"] == "delenje":
            data["kolicnik"] = data['broj1']/data["broj2"]
    return Response(data)


@api_view(["POST"])
def prv_post_metod(request):
     print(request.data)
     return Response({"Status":"uspeshno"})
    

@api_view(['POST'])
def soberi_broevi_post(request):
    broj1 = int(request.data['broj1'])
    broj2 = int(request.data.get('broj2',0))
    zbir = broj1 + broj2

    response_dict = {
     "broj1":broj1,
     "broj2":broj2,
     "zbir" :zbir   
    }
    
    return Response(response_dict)

class prvaKlasaAPI(APIView):
     
     def get(self,request):
          return Response({"status":"uspeshen get"})
     
     def post(self,request):
          return Response({"status":"uspeshen post"})
     

class checkGetOrPost(APIView):
     
     def get(self,request):
          return_data= {}
          return_data["broj"]  = int(request.GET["broj"])
          return_data["kvadrat"] =  return_data["broj"] ** 2

                     
          return Response(return_data)
          
     def post(self,request):
          return_data= {}
          return_data["broj"]  = int(request.GET["broj"])

          if return_data["broj"] % 2 == 0:
              return_data["paren"] = 'true'
          else:
              return_data["paren"] = 'false'

          return Response(return_data)
     

class LiceAPI(APIView):
     
     def get(self, request):
          siteLica = Lice.objects.all().order_by("id")
          lica_serializer = LiceSerializers(siteLica,many = True)
          return Response(lica_serializer.data)
     
     def post(self, request):
          lica_serializer = LiceSerializers(data = request.data)
          if lica_serializer.is_valid():
            lica_serializer.save()
            return Response(lica_serializer.data)
          else:
               return Response(lica_serializer.errors)
          
     def delete(self,request):
          #korisnikot kazuva sto saka da s eizbrishe , go naogame podatokot i go brisheme
          lice = Lice.objects.get(id = request.data.get("id"))
          lice.delete()
          return Response({"info":"The person is deleted"})
     
     def patch(self, request):
          #korsinikot sto saka da updetira i koi se novite podatoci so koi saka da se updatetira 
          lice = Lice.objects.get(id = request.data.get("id"))
          lica_serializer = LiceSerializers(lice, data = request.data, partial = True)
          if lica_serializer.is_valid():
               lica_serializer.save()
               return Response(lica_serializer.data)
          else:
               return Response(lica_serializer.errors)
          
     

class LiceFilter(APIView):
     
     def get(self, request):
          ##siteLica= Lice.objects.filter(grad='Skopje',prezime = 'Mitrov') filtrira preku kod 
          ##siteLica= Lice.objects.filter(grad=request.GET.get('grad','')) po parametar
          ##siteLica= Lice.objects.filter(grad__contains=request.GET.get('grad','')) koj sodrzi like%
          siteLica= Lice.objects.filter(godini__gte=request.GET.get('godini',''))##greather
          lica_serializer = LiceSerializers(siteLica,many = True)
          return Response(lica_serializer.data)
     
     
     
"""class FilmAPI(APIView):
     
     def get(self, request):
          siteFilmov = Film.objects.all().order_by("godina")
          Film_serializer = FilmSerializers(siteFilmov,many = True)
          return Response(Film_serializer.data)"""