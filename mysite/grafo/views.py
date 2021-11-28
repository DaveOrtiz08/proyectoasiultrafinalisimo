from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Tessiu
from scipy.spatial import distance

# Create your views here.
def grafo(request):

    #return HttpResponse("Home")
    
    l= Tessiu.objects.get_queryset()
    template_name = "grafo/grafo.html"
    listaProcesada = procesaLista(l)
    distancia= euclidea(l)
    return render(request, template_name, {'lista':l,'listaproc':listaProcesada,'euclidea':distancia})
    
        
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

def euclidea(tejidos):
    tejidosTotal = []
    for i in tejidos:
        tejido = []
        tejido.append(i.temperatura)
        tejido.append(i.color)
        tejido.append(i.inflamation)
        tejidosTotal.append(tejido)      

    mEuclidea = []
    for i in range(len(tejidosTotal)):
        f = []
        for j in range(len(tejidosTotal)):
            f.append(round(distance.euclidean(tejidosTotal[i],tejidosTotal[j], 6 )))
        mEuclidea.append(f)

    return mEuclidea

def calculaUmbral(request):
    template_name = "grafo/grafo.html"
    umbral=0
    if request.method  == 'GET':
        umbral=float(request.GET.get('umbral'))
    L = Tessiu.objects.get_queryset()
    listaprocesada = distancia(L,umbral)
    diccionario = {'listap':listaprocesada}
    return render(request, template_name, diccionario)


def distancia(datos,a):
    final = []
    dist = []
    tabla1 = []
    for i in datos:
        dato = []
        dato.append(i.temperatura),dato.append(i.color),dato.append(i.inflamation)
        final.append(dato)      
    
    for i in range(len(final)):
        aux = []
        for j in range(len(final)):
            aux.append(distance.euclidean(final[i],final[j],3))
        dist.append(aux)
    
   
    for i in range(len(dist)):
        for j in range(i,len(dist)):
            v0 = i
            vf = j
            mag = dist[i][j]
            if  mag <= a:
             tabla1.append((v0,vf,mag,"TRUE"))
            elif mag >= a:
             tabla1.append((v0,vf,mag,"FALSE"))
    return tabla1
   

