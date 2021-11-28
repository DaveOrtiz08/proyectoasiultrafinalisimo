from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tessiu


# Create your views here.
def home(request):

    #return HttpResponse("Home")
    
    l= Tessiu.objects.get_queryset()
    template_name = "home/index.html" 
    listaProcesada = procesaLista(l)
    
    return render(request, template_name, {'lista':l,'listaproc':listaProcesada,})
    
        
def nohome(request):
    print("SALUDOS A LA BANDA")
    
    return HttpResponse("BANDA")

def procesaLista(lista):
    #Hacer algo con la lista
    lista1=[]
    for elemento in lista:
        valor=elemento.temperatura**2 + elemento.inflamation**2 + elemento.color**2
        p=valor**0.5
        if  p > 100:
            lista1.append(p)
    return lista1


   

